# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_files', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default', max_length=64)),
                ('file', models.FileField(blank=True, null=True, upload_to='media/%Y/%m/%d')),
            ],
        ),
    ]
