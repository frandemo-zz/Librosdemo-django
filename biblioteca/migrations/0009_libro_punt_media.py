# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0008_auto_20150731_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='punt_media',
            field=models.DecimalField(default=0, verbose_name='Promedio', editable=False, max_digits=3, decimal_places=2),
        ),
    ]
