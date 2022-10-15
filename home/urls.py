from django.urls import path
from home import views


urlpatterns = [
    path('', views.index, name='index'),
    path('ver-usuarios/', views.ver_usuarios, name='ver_usuarios'),
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),
    path('about/', views.about, name='about'),
]