# Generated by Django 2.0.1 on 2018-01-17 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20180117_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
