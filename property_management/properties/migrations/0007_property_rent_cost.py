# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0006_auto_20150901_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='rent_cost',
            field=models.CharField(max_length=50, null=b'true'),
        ),
    ]
