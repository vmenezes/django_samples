# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 08:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='park',
            old_name='localtion',
            new_name='location',
        ),
    ]
