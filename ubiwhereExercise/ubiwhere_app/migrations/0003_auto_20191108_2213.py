# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-08 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubiwhere_app', '0002_auto_20191107_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datafromsensor',
            name='category',
            field=models.CharField(max_length=255),
        ),
    ]