# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 08:06
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('desc', models.TextField()),
                ('contry', models.CharField(max_length=250)),
                ('state', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('address', models.TextField()),
                ('localtion', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
