# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-11 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0007_auto_20161111_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidadmedidac',
            name='cant_equivalencia',
            field=models.PositiveIntegerField(verbose_name='Cantidad de equivalencia'),
        ),
    ]
