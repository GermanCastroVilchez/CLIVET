# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-20 20:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0005_auto_20161020_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atencion',
            name='Vacunacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinica.Vacunacion'),
        ),
        migrations.AlterField(
            model_name='atencion',
            name='consulta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinica.Consulta'),
        ),
        migrations.AlterField(
            model_name='atencion',
            name='notas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinica.Notas'),
        ),
    ]
