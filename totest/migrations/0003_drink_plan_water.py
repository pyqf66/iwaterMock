# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-21 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totest', '0002_drink_plan_hydrating_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink_plan',
            name='water',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
