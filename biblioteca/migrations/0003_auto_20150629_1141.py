# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_libro_archivo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Tipo de Archivo')),
                ('descripcion', models.CharField(max_length=256, verbose_name='Descripci\xf3n de el tipo')),
            ],
        ),
        migrations.AddField(
            model_name='libro',
            name='img',
            field=models.FileField(default=b'null', upload_to=b'documents/portada', verbose_name='Imagen de portada'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='archivo',
            field=models.FileField(default=b'null', upload_to=b'documents/libros', verbose_name='Archivo del Libro'),
        ),
        migrations.AddField(
            model_name='libro',
            name='tipo',
            field=models.ManyToManyField(to='biblioteca.Tipo'),
        ),
    ]
