# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0007_property_rent_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='bathrooms',
            field=models.CharField(max_length=2, null=b'true'),
        ),
        migrations.AddField(
            model_name='property',
            name='bedrooms',
            field=models.CharField(max_length=2, null=b'true'),
        ),
        migrations.AddField(
            model_name='property',
            name='car_spaces',
            field=models.CharField(max_length=2, null=b'true'),
        ),
        migrations.AddField(
            model_name='property',
            name='property_type',
            field=models.CharField(max_length=50, null=b'true'),
        ),
    ]
