# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170212_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutriuser',
            name='birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='nutriuser',
            name='bmi',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='nutriuser',
            name='gender',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='nutriuser',
            name='rda',
            field=models.FloatField(null=True),
        ),
    ]
