# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0012_property_suburb'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='furnished_state',
            field=models.BooleanField(default=False),
        ),
    ]
