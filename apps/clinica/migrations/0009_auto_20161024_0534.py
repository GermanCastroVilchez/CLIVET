# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-24 05:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0008_auto_20161024_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial',
            name='mascota',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clinica.Mascota', verbose_name='Mascota'),
        ),
    ]
