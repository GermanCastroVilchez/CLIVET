# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-24 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atencion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ath', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creada')),
            ],
            options={
                'verbose_name_plural': 'Atenciones',
                'verbose_name': 'Atencion',
            },
        ),
        migrations.CreateModel(
            name='ColaMedica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creada')),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('normal', 'Normal'), ('emergencia', 'Emergencia'), ('reservado', 'Reservado')], max_length=100)),
            ],
            options={
                'verbose_name_plural': 'ColasMedicas',
                'verbose_name': 'ColaMedica',
            },
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anamnesis', models.CharField(max_length=200)),
                ('diagnostico', models.CharField(max_length=300)),
                ('dx', models.CharField(max_length=300)),
                ('hallasgos_clinicos', models.CharField(max_length=100)),
                ('motivo_atencion', models.CharField(max_length=300)),
                ('observacion', models.CharField(max_length=300)),
                ('pronostico', models.CharField(max_length=300)),
                ('pruebas_auxiliares', models.CharField(max_length=300)),
                ('tratamiento', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Consultas',
                'verbose_name': 'Consulta',
            },
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_historia', models.CharField(max_length=40)),
                ('created_ath', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creada')),
            ],
            options={
                'verbose_name_plural': 'Historias',
                'verbose_name': 'Historia',
            },
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField(null=True, verbose_name='Fecha Nacimiento')),
                ('genero', models.CharField(choices=[('Macho', 'Macho'), ('Hembra', 'Hembra')], default='Macho', max_length=10)),
                ('especie', models.CharField(choices=[('Perro', 'Perro'), ('Gato', 'Gato'), ('Roedor', 'Roedor')], default='Perro', max_length=10)),
                ('raza', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('cond_corporal', models.CharField(choices=[('Buena', 'Buena'), ('Regular', 'Regular'), ('Demacrada', 'Demacrada')], default='Buena', max_length=10)),
                ('esterelizado', models.CharField(choices=[('Si', 'Sí'), ('No', 'No')], default=True, max_length=10, verbose_name='Esterelizado...?')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_actived', models.BooleanField(default=False, verbose_name='Actived')),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Mascotas',
                'verbose_name': 'Mascota',
            },
        ),
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Notas',
                'verbose_name': 'Nota',
            },
        ),
        migrations.CreateModel(
            name='Vacunacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_programada', models.DateTimeField()),
                ('Observacion', models.CharField(max_length=100)),
                ('vacuna', models.CharField(choices=[('VACUNA1', 'Vacuna1'), ('VACUNA2', 'Vacuna2'), ('VACUNA3', 'Vacuna3'), ('VACUNA4', 'Vacuna4')], max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Vacunaciones',
                'verbose_name': 'Vacunacion',
            },
        ),
    ]
