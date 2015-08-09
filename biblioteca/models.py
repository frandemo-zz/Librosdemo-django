# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Libro(models.Model):
    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Todos los libros"
        ordering=['fecha']

    titulo = models.CharField(u'Título', max_length=100)
    descripcion = models.TextField(u'Descripción')
    autor = models.CharField(u'Autor', max_length=100)
    fecha = models.DateField(u'Fecha de Publicación')
    archivo = models.FileField(u'Archivo del Libro' ,upload_to = 'libros', default='null')  
    tipo = models.ManyToManyField('Tipo')
    img = models.FileField(u'Imagen de portada',upload_to = 'portada', default='null')
    categoria = models.ManyToManyField(u'Categoria')
    punt_media = models.DecimalField(u'Promedio',  default=0, editable=False, max_digits=3, decimal_places=2)

    def __str__(self):
        return self.titulo


class Categoria(models.Model):
    nombre = models.CharField(u'Título de la Categoría', max_length=100)
    descripcion = models.CharField(u'Descripción de la Categoría', max_length=256)


    def __str__(self):
        return self.nombre
        

class Tipo(models.Model):
    nombre = models.CharField(u'Tipo de Archivo', max_length=100)
    descripcion = models.CharField(u'Descripción de el tipo', max_length=256)


    def __str__(self):
        return self.nombre
    
class Valoracion(models.Model):
    class Meta:
        verbose_name = "Reseña"
        verbose_name_plural = "Todos las reseñas"
        ordering=['fecha']
        
    nombre = models.CharField(u'Nombre', max_length=40, default="Anónimo")
    valoracion = models.IntegerField(u'Valoración', null=True)
    pub = models.TextField(u'Publicación', max_length=200, null=True)
    fecha = models.DateTimeField(u'Fecha de la reseña', auto_now_add=True, null=True)
    published_in = models.ForeignKey(Libro, null=True)
    
    def __str__(self):
        return self.nombre
    