from django.urls import path
from home import views

urlpatterns = [
    path('', views.index),
    path('ver-familiar/', views.ver_familiares),
    path('crear-familiar/<str:nombre>/<str:apellido>/', views.crear_familiar),
]