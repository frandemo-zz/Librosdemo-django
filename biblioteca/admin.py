from django.contrib import admin
from biblioteca.models import Libro, Categoria, Tipo, Valoracion
# Register your models here.

admin.site.register(Libro)
admin.site.register(Categoria)
admin.site.register(Tipo)
admin.site.register(Valoracion) 