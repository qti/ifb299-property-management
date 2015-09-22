# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0009_auto_20150916_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='bathrooms',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='property',
            name='bedrooms',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='property',
            name='car_spaces',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_type',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='property',
            name='rent_cost',
            field=models.IntegerField(default=0),
        ),
    ]
