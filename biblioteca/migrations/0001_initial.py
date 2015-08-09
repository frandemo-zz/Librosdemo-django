# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='T\xedtulo de la Categor\xeda')),
                ('descripcion', models.CharField(max_length=256, verbose_name='Descripci\xf3n de la Categor\xeda')),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100, verbose_name='T\xedtulo')),
                ('descripcion', models.TextField(verbose_name='Descripci\xf3n')),
                ('autor', models.CharField(max_length=100, verbose_name='Autor')),
                ('fecha', models.DateTimeField(verbose_name='Fecha de Publicaci\xf3n')),
                ('categoria', models.ManyToManyField(to='biblioteca.Categoria')),
            ],
            options={
                'ordering': ['-fecha'],
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Todos los libros',
            },
        ),
    ]
