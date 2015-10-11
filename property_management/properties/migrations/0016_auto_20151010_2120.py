# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0015_property_furnished_state_char'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'permissions': (('view_property', 'Can view property'),)},
        ),
    ]
