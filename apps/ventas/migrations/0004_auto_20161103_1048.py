# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-03 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_auto_20161103_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]
