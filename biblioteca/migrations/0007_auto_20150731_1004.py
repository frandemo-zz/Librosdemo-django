# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0006_auto_20150731_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='valoracion',
            field=models.IntegerField(default=0, verbose_name='Valoraci\xf3n', editable=False),
        ),
    ]
