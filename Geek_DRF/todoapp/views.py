from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectSerializer, ToDoSerializer
from .models import Project, ToDo
from email.policy import default
from http import server
from .filters import ProjectFilter, ToDoFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import mixins, viewsets


class ProjectLimitOffsetPaginations(LimitOffsetPagination):
    default_limit = 10


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    filterset_class = ProjectFilter
    pagination_class = ProjectLimitOffsetPaginations


class ToDoLimitOffsetPaginations(LimitOffsetPagination):
    default_limit = 20


class ToDoViewSet(ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.object.all()
    filterset_class = ToDoFilter
    pagination_class = ToDoLimitOffsetPaginations

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.active_toggle(instance)
        ser = self.get_serializer(instance).data
        serializer = self.get_serializer(instance, data=ser)
        serializer.is_valid(raise_excepion=True)
        serializer.save()
        return Response(serializer.data)

    def active_toggle(self, instance):
        instance.is_active=True

