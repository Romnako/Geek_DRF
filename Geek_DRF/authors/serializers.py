from rest_framework.serializers import ModelSerializer
from .models import Author, Biography, Book, Article
from rest_framework.serializers import StringRelatedField, PrimaryKeyRelatedField

class SimpleAuthorModeSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookModelSerializer(ModelSerializer):
    authors = StringRelatedField(many=True)
    class Meta:
        model = Book
        fields = '__all__'


class ArticleModeSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class BiographyModelSerializer(ModelSerializer):
    author = SimpleAuthorModeSerializer()
    class Meta:
        model = Biography
        fields = '__all__'