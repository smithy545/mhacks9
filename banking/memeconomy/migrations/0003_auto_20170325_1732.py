# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-25 21:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memeconomy', '0002_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
