# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0007_auto_20150731_1004'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='libro',
            options={'ordering': ['fecha'], 'verbose_name': 'Libro', 'verbose_name_plural': 'Todos los libros'},
        ),
        migrations.AlterModelOptions(
            name='valoracion',
            options={'ordering': ['fecha'], 'verbose_name': 'Rese\xf1a', 'verbose_name_plural': 'Todos las rese\xf1as'},
        ),
        migrations.RemoveField(
            model_name='libro',
            name='valoracion',
        ),
        migrations.RemoveField(
            model_name='valoracion',
            name='autor',
        ),
        migrations.AddField(
            model_name='valoracion',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de la rese\xf1a', null=True),
        ),
        migrations.AddField(
            model_name='valoracion',
            name='nombre',
            field=models.CharField(default=b'An\xc3\xb3nimo', max_length=100, verbose_name='Nombre'),
        ),
        migrations.AddField(
            model_name='valoracion',
            name='pub',
            field=models.TextField(null=True, verbose_name='Publicaci\xf3n'),
        ),
        migrations.AddField(
            model_name='valoracion',
            name='published_in',
            field=models.ForeignKey(to='biblioteca.Libro', null=True),
        ),
        migrations.AddField(
            model_name='valoracion',
            name='valoracion',
            field=models.IntegerField(null=True, verbose_name='Valoraci\xf3n'),
        ),
    ]
