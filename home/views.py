from datetime import datetime
from django.shortcuts import render, redirect
from home.models import Persona
from home.forms import HumanoFormulario, BusquedaHumanoFormulario


def crear_usuario(request):
    if request.method == 'POST':
        formulario = HumanoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            fecha_nacimiento = data.get('fecha_nacimiento', None)

            persona = Persona(nombre=nombre,
                              apellido=apellido,
                              edad=edad,
                              fecha_nacimiento=fecha_nacimiento)
            persona.save()

            return redirect('ver_usuarios')
        else:
            return render(request,
                          'home/crear_usuarios.html',
                          {'formulario': formulario})

    formulario = HumanoFormulario()

    return render(request,
                  'home/crear_usuario.html',
                  {'formulario': formulario})


def ver_usuarios(request):
    nombre = request.GET.get('nombre', None)

    if nombre:
        personas = Persona.objects.filter(nombre__icontains=nombre)
    else:
        personas = Persona.objects.all()

    formulario = BusquedaHumanoFormulario()

    return render(request,
                  'home/ver_usuarios.html',
                  {'personas': personas,'formulario': formulario})


def about(request):
    return render(request, 'home/about.html')


def index(request):
    return render(request, 'home/index.html')