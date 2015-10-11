# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_auto_20150828_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
