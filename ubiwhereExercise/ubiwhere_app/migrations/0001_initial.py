# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-07 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataFromSensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('geo_location', models.CharField(max_length=255)),
                ('created_by', models.TextField()),
                ('state', models.IntegerField()),
                ('category', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
    ]
