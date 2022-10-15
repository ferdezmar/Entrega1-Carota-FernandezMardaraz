from django.urls import path
from home import views


urlpatterns = [
    path('', views.index, name='index'),
    path('ver-familiar/', views.ver_personas, name='ver_personas'),
    path('crear-familiar/', views.crear_persona, name= 'crear_persona'),
]