from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
import random
from home.models import Persona
from home.forms import HumanoFormulario, BusquedaHumanoFormulario

# def saludo(request):
#     return HttpResponse ('<h1> Buenas y santas </h1>')

# def fecha (request):
#     fecha_actual = datetime.now()
#     return HttpResponse (f'La hora y fecha actual es {fecha_actual}')

# def calcular_fecha_nac(request, edad):
#     fecha = datetime.now().year - edad
#     return HttpResponse(f'Tu fecha de nacimiento aproximada para tus {edad} años, es {fecha}')

# def mi_template (request):
    
#     cargar_archivo = open(r'C:\Users\fedef\OneDrive\Documentos\Python\Proyecto\templates\mi_template.html', 'r')
#     template = Template(cargar_archivo.read())
#     cargar_archivo.close()
    
#     contexto = Context()
    
#     template_renderizado = template.render(contexto)
    
#     return HttpResponse(template_renderizado)

# def tu_template (request, nombre):
    
#     template = loader.get_template('tu_template.html')
#     template_renderizado = template.render({'persona': nombre})
        
#     return HttpResponse(template_renderizado)

# def prueba_template(request):
    
#     mi_contexto = {
#         'rango': list(range (1,11)),
#         'valor_aleatorio': random.randrange(1,11)
#         }
    
    # template = loader.get_template('prueba_template.html')
    # template_renderizado = template.render(mi_contexto)
        
    # return HttpResponse(template_renderizado)

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
        
            return redirect('ver_familiares')
    
    formulario = HumanoFormulario()
    
    return render(request, 'home/crear_familiar.html', {'formulario': formulario})

def ver_familiares(request):
    
    nombre = request.GET.get('nombre', None)
    
    if nombre:
        familiares = Persona.objects.filter(nombre__icontains=nombre)
    else:
        familiares = Persona.objects.all()
    
    formulario = BusquedaHumanoFormulario()
    
    return render(request, 'home/ver_familiares.html', {'familiares': familiares})
                  
    # , {'formulario': formulario} )

def index (request):
    
    return render(request, 'home/index.html')