from datetime import datetime
from django.shortcuts import render, redirect
from home.models import Persona
from home.forms import HumanoFormulario, BusquedaHumanoFormulario


def crear_persona(request):
    if request.method == 'POST':
        formulario = HumanoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            fecha_nacimiento = data.get('fecha_nacimiento', datetime.now())

            persona = Persona(nombre=nombre,
                              apellido=apellido,
                              edad=edad,
                              fecha_nacimiento=fecha_nacimiento)
            persona.save()

            return redirect('ver_personas')
        else:
            return render(request,
                          'home/crear_persona.html',
                          {'formulario': formulario})

    formulario = HumanoFormulario()

    return render(request,
                  'home/crear_persona.html',
                  {'formulario': formulario})


def ver_personas(request):
    nombre = request.GET.get('nombre', None)

    if nombre:
        familiares = Persona.objects.filter(nombre__icontains=nombre)
    else:
        familiares = Persona.objects.all()

    formulario = BusquedaHumanoFormulario()

    return render(request,
                  'home/ver_personas.html',
                  {'familiares': familiares,'formulario': formulario})


def index (request):
    return render(request, 'home/index.html')