# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 01:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessageCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recepient', models.CharField(help_text='receives message', max_length=20)),
                ('sender', models.CharField(help_text='sent message', max_length=20)),
                ('subject', models.CharField(help_text='summary of the message', max_length=78)),
                ('content', models.TextField(help_text='content')),
            ],
        ),
    ]
