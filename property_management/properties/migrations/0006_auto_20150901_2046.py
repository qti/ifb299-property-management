# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_auto_20150901_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='name',
            field=models.CharField(default=b'House listing', max_length=255),
        ),
    ]
