# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-15 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpagecse', '0017_auto_20171115_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='id',
        ),
        migrations.AlterField(
            model_name='faculty',
            name='user',
            field=models.CharField(default='1', max_length=300, primary_key=True, serialize=False),
        ),
    ]
