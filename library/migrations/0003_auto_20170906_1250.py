# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20170906_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='e-mail'),
        ),
    ]
