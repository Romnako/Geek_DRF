import graphene
from graphene_django import DjangoObjectType
from authors.models import Author
from todoapp.models import ToDo, Project


class UserType(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_todos = graphene.List(ToDoType)
    all_projects = graphene.List(ProjectType)

    def resolve_all_users(root, info):
        return Author.objects.all()

    def resolve_all_todos(root, info):
        return ToDo.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()


schema = graphene.Schema(query=Query)