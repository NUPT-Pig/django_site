# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-05 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20180115_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='term',
            field=models.IntegerField(default=0),
        ),
    ]
