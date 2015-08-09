# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('biblioteca', '0005_auto_20150702_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Valoracion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='libro',
            name='valoracion',
            field=models.IntegerField(default=1, verbose_name='Valoraci\xf3n', editable=False),
        ),
    ]
