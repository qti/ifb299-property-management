# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0013_property_furnished_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='house_number',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='property',
            name='postcode',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='property',
            name='state',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='property',
            name='street',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
