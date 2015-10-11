# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_property_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='pets_allowed',
            field=models.BooleanField(default=False),
        ),
    ]
