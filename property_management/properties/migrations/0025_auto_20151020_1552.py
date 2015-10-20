# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0024_auto_20151013_2139'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name_plural': 'Properties'},
        ),
        migrations.AddField(
            model_name='property',
            name='contract_information',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
