# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_auto_20150629_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='archivo',
            field=models.FileField(default=b'null', upload_to=b'libros', verbose_name='Archivo del Libro'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='img',
            field=models.FileField(default=b'null', upload_to=b'portada', verbose_name='Imagen de portada'),
        ),
    ]
