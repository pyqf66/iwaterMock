# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-12 02:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totest', '0007_mock_any_api_manual'),
    ]

    operations = [
        migrations.AddField(
            model_name='api_mock',
            name='api_no',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
