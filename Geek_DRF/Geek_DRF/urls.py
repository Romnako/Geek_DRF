from rest_framework.authtoken import views
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from authors.views import AuthorModelViewSet, ArticleModeViewSet, BiographyModelViewset, BookModelViewSet
from todoapp.views import ToDoViewSet, ProjectViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from graphene_django.views import GraphQLView


schema_view = get_schema_view(
    openapi.Info(
        title="ToDo App",
        default_version='0.1',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


router = DefaultRouter()
router.register('Authors', AuthorModelViewSet)
router.register('Article', ArticleModeViewSet)
router.register('Biography', BiographyModelViewset)
router.register('Book', BookModelViewSet)
router.register('todos', ToDoViewSet)
router.register('projects', ProjectViewSet)
router.register('test', AuthorModelViewSet, basename='lal')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('testview/', AuthorModelViewSet.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
    # path('test/<str:name>', AuthorModelViewSet.as_view())
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
                schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path("graphql/", GraphQLView.as_view(graphiql=True)),

]
