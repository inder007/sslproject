# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-28 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpagecse', '0021_faculty_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='last_name',
            field=models.CharField(default='', max_length=300),
        ),
    ]