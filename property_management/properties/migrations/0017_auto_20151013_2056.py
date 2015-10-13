# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('properties', '0016_auto_20151010_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='manager',
            field=models.ForeignKey(related_name='manager', default=1, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='owner',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
