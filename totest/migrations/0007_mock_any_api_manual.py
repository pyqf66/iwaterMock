# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-09 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totest', '0006_api_mock_is_open'),
    ]

    operations = [
        migrations.CreateModel(
            name='mock_any_api_manual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_content', models.TextField(null=True)),
            ],
        ),
    ]
