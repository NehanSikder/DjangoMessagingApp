# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 02:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0002_auto_20171023_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inbox',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
    ]
