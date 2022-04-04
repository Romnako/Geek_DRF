# from rest_framework.viewsets import ModelViewSet
# from rest_framework import serializers
# from rest_framework.decorators import api_view, renderer_classes
# from rest_framework.parsers import JSONParser
from requests import Response
from rest_framework import mixins, viewsets
from rest_framework.views import APIView

import authors
from .models import Author, Book, Biography, Article
from .serializers import AuthorModelSerializer, BookModelSerializer, ArticleModeSerializer, BiographyModelSerializer, \
    SimpleAuthorModeSerializer


class AuthorView(APIView):

    def get(self, request):
        author = Author.object.all()
        serializer = SimpleAuthorModeSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        return Response('Answer the post!')


class AuthorModelViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                         viewsets.GenericViewSet):

    serializer_class = AuthorModelSerializer
    queryset = Author.objects.all()
    filtered_field = ['first_name']


class BookModelViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    queryset = Book.object.all
    serializer_class = BookModelSerializer


class ArticleModeViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                         viewsets.GenericViewSet):
    queryset = Article.object.all()
    serializer_class = ArticleModeSerializer


class BiographyModelViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    queryset = Biography.object.all()
    serializer_class = BiographyModelSerializer




