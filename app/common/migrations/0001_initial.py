# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-09 12:51
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modify')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=75, verbose_name='Nombre')),
                ('etiqueta', models.TextField(blank=True, null=True, verbose_name='Etiquetas')),
                ('archivo', models.FileField(blank=True, null=True, upload_to='archivo/%Y/%m/%d/', verbose_name='Archivo')),
            ],
            options={
                'db_table': 'archivos',
                'verbose_name': 'Archivo',
                'verbose_name_plural': 'Archivos',
                'default_related_name': 'archivo',
            },
        ),
        migrations.CreateModel(
            name='Carpeta',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modify')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=75, verbose_name='Titulo')),
                ('etiqueta', models.TextField(blank=True, null=True, verbose_name='Etiquetas')),
                ('color', colorfield.fields.ColorField(default='#FF0000', max_length=18, verbose_name='Color')),
                ('icono', models.CharField(max_length=25, verbose_name='Icono')),
                ('padre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carpeta', to='common.Carpeta')),
            ],
            options={
                'db_table': 'carpetas',
                'verbose_name': 'Carpeta',
                'verbose_name_plural': 'Carpetas',
                'default_related_name': 'carpeta',
            },
        ),
        migrations.AddField(
            model_name='archivo',
            name='carpetas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='archivo', to='common.Carpeta'),
        ),
    ]
