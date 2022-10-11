from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
import random
from home.models import Persona
from home.forms import HumanoFormulario, BusquedaHumanoFormulario


def crear_familiar(request):
    
    if request.method == 'POST':
        
        formulario = HumanoFormulario(request.POST)
        
        if formulario.is_valid():
            
            data= formulario.cleaned_data
            
            nombre= data ['nombre']
            apellido= data ['apellido']
            edad= data ['edad']
            fecha_nacimiento = data.get('fecha_nacimiento', datetime.now())
            familiar = Persona(nombre=nombre, apellido=apellido, edad=edad, fecha_nacimiento=fecha_nacimiento)
            familiar.save()
        
            return redirect('ver_personas')
    
    formulario = HumanoFormulario()
    
    return render(request, 'home/crear_familiar.html', {'formulario': formulario})

def ver_familiares(request):
    
    nombre = request.GET.get('nombre', None)
    
    if nombre:
        familiares = Persona.objects.filter(nombre__icontains=nombre)
    else:
        familiares = Persona.objects.all()
    
    formulario = BusquedaHumanoFormulario()
    
    return render(request, 'home/ver_familiares.html', {'familiares': familiares,'formulario': formulario} )

def index (request):
    
    return render(request, 'home/index.html')