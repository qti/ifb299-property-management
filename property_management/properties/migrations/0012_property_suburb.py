# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0011_auto_20150922_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='suburb',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
