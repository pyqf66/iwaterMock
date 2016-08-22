# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-01 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totest', '0003_drink_plan_water'),
    ]

    operations = [
        migrations.CreateModel(
            name='iwater_api',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('environment', models.CharField(max_length=10, null=True)),
                ('url', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
