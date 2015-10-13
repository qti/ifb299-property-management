# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0019_auto_20151013_2118'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={},
        ),
        migrations.AddField(
            model_name='property',
            name='tenant_information',
            field=models.TextField(default=b''),
        ),
    ]
