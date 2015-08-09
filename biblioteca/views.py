from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
from django.db.models import Avg
from biblioteca.models import Libro, Valoracion
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import requires_csrf_token
from django.core.mail import send_mail
import os
# Create your views here.
def inicio(request):
    context = RequestContext(request)
    libros = Libro.objects.order_by('-punt_media')[:5]
    #os.system("zenity --info --text \""+libros+"\"")
    return render_to_response('index.html', 
                              {'libros':libros},
                              context)
def biblioteca(request):
    context = RequestContext(request)
    libros = Libro.objects.all()
    return render_to_response('biblioteca.html', 
                              {'libros':libros},
                              context)
def ajustes(request):
    context = RequestContext(request)
    return render_to_response('ajustes.html', 
                              context)
def nuevolibro(request):
    context = RequestContext(request)
    return render_to_response('nuevolibro.html', 
                              context)
@requires_csrf_token
def libroT(request, libId):
    context = RequestContext(request)
    librete = Libro.objects.get(id=libId)

    if request.method == 'POST':
        val=Valoracion()
        val.nombre=request.POST['nombre']
        val.valoracion=request.POST['valoracion']
        val.pub=request.POST['pub']
        val.published_in=librete
        val.save()

    res=Valoracion.objects.filter(published_in=librete)
    avgEs=res.aggregate(Avg('valoracion'))['valoracion__avg']
    print(avgEs)
    if avgEs!=None:
        librete.punt_media=avgEs
        librete.save()

    return render_to_response('libro.html',
                                  {'libroI':librete,
                                   'valor':res,
                                  'avgEs':avgEs},
                                  context)
@requires_csrf_token
def nuevo_usuario(request):
    context = RequestContext(request)
    if request.method=='POST':
        n_u=User()
        n_u.username=request.POST['username']
        n_u.email=request.POST['email']
        password=request.POST['password']
        n_u.set_password(password)
        n_u.save()
    return render_to_response('nuevousuario.html',
                              context)
@requires_csrf_token
def valorar(request):
    context = RequestContext(request)
    valor= None

    if request.method == 'POST':
        librete = Libro.objects.get(id=request.POST['id'])
        val=Valoracion()
        val.nombre=request.POST['nombre']
        val.valoracion=request.POST['valoracion']
        val.pub=request.POST['pub']
        val.published_in=librete
        val.save()
        valor=Valoracion.objects.filter(published_in=librete)
    return render_to_response('opinion.html', 
                                {'valor':valor},
                                context)  

@requires_csrf_token
def crear_libro(request):
    context = RequestContext(request)
    if request.method=='POST':
        lib=Libro()
        lib.titulo=request.POST['titulo']
        lib.autor=request.POST['autor']
        lib.fecha=request.POST['fecha']
        lib.descripcion=request.POST['descripcion']
        lib.archivo=request.FILES['archivo']
        lib.img=request.FILES['img']
        lib.save()
        
    return render_to_response('nuevolibro.html',
                              context)
@requires_csrf_token
def enviar_mail(request):
    context = RequestContext(request)
    if request.method=='POST':
        send_mail(request.POST['asunto'], request.POST['mensaje'], 'franciscodemaussion@gmail.com',
    [request.POST['mail']], fail_silently=False)
    return render_to_response('ajustes.html',
                              context)