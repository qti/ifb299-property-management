# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0014_auto_20150923_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='furnished_state_char',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
