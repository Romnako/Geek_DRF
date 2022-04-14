from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Project
from .models import ToDo
from .models import Author


class ProjectSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class ToDoSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = ToDo
        exclude = ('is_active',)
        fields = '__all__'


class AuthorSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Author
        #fields = '__all__'
        fields = [
            "url",
            "username",
            "first_name",
            "last_name",
            "email",
        ]


class AuthorSerializerNew(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = [
            "url",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_superuser"
        ]