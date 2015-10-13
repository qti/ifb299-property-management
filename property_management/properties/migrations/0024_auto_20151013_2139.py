# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0023_auto_20151013_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='tenant_information',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
