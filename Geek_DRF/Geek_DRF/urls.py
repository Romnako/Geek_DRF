"""Geek_GRF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authors.views import AuthorModelViewSet, ArticleModeViewSet, BiographyModelViewset, BookModelViewSet
from todoapp.views import ToDoViewSet, ProjectViewSet


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
    # path('test/<str:name>', AuthorModelViewSet.as_view())
]
