# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0008_auto_20150908_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='image2',
            field=models.CharField(default=b'', max_length=128, blank=True),
        ),
        migrations.AddField(
            model_name='property',
            name='image3',
            field=models.CharField(default=b'', max_length=128, blank=True),
        ),
    ]
