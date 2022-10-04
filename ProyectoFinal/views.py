from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
import random
from home.models import Persona

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

def crear_familiar(request, nombre, apellido):
    
    familiar = Persona(nombre=nombre, apellido=apellido, edad=random.randrange(1,99), fecha_nacimiento=datetime.now())
    familiar.save()
    
    template = loader.get_template('crear_familiar.html')
    template_renderizado = template.render({'familiar': familiar})
    
    return HttpResponse(template_renderizado)

def ver_familiares(request):
    
    familiares = Persona.objects.all()
    
    template = loader.get_template('ver_familiares.html')
    template_renderizado = template.render({'familiares': familiares})
              
    return HttpResponse(template_renderizado)