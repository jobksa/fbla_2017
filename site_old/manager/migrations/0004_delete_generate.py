# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-02 19:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_generate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='generate',
        ),
    ]