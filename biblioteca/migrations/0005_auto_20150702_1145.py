# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0004_auto_20150630_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='fecha',
            field=models.DateField(verbose_name='Fecha de Publicaci\xf3n'),
        ),
    ]
