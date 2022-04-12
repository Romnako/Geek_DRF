from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectSerializer, ToDoSerializer, AuthorSerializer, AuthorSerializerNew
from .models import Project, ToDo, Author
from email.policy import default
from http import server
from .filters import ProjectFilter, ToDoFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import mixins, viewsets, permissions


class AuthorViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


    def get_serializer_class(self):
        if self.request.version == '0.2':
            return AuthorSerializerNew
        return AuthorSerializer



class ProjectLimitOffsetPaginations(LimitOffsetPagination):
    default_limit = 10


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    filterset_class = ProjectFilter
    pagination_class = ProjectLimitOffsetPaginations
    permission_classes = [permissions.AllowAny]


class ToDoLimitOffsetPaginations(LimitOffsetPagination):
    default_limit = 20


class ToDoViewSet(ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.object.all()
    filterset_class = ToDoFilter
    pagination_class = ToDoLimitOffsetPaginations
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.active_toggle(instance)
        ser = self.get_serializer(instance).data
        serializer = self.get_serializer(instance, data=ser)
        serializer.is_valid(raise_excepion=True)
        serializer.save()
        return Response(serializer.data)

    def active_toggle(self, instance):
        instance.is_active = False

