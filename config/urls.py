
from django.contrib import admin
from django.urls import path, include
from escola import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', views.AlunosViewSet, basename='Alunos')
router.register('Cursos', views.CursosViewSet, basename='Cursos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]