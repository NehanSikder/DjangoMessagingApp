# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0003_auto_20171025_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inbox',
            name='sender',
            field=models.CharField(help_text='sent message', max_length=20),
        ),
    ]
