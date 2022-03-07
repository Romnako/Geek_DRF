from rest_framework.viewsets import ModelViewSet
from .models import Author, Book, Biography, Article
from rest_framework import serializers
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import JSONParser

from .serializers import AuthorModelSerializer, BookModelSerializer, ArticleModeSerializer, BiographyModelSerializer


class AuthorModelViewSet(ModelViewSet):

    serializer_class = AuthorModelSerializer
    queryset = Author.objects.all()


class BookModelViewSet(ModelViewSet):
    queryset = Book.object.all
    serializer_class = BookModelSerializer


class ArticleModeViewSet(ModelViewSet):
    queryset = Article.object.all()
    serializer_class = ArticleModeSerializer


class BiographyModelViewset(ModelViewSet):
    queryset = Biography.object.all()
    serializer_class = BiographyModelSerializer

