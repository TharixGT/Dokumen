# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-10 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivo',
            name='archivo',
            field=models.FileField(upload_to='archivo/%Y/%m/%d/', verbose_name='Archivo'),
        ),
        migrations.AlterField(
            model_name='archivo',
            name='nombre',
            field=models.CharField(max_length=255, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='carpeta',
            name='titulo',
            field=models.CharField(max_length=255, verbose_name='Titulo'),
        ),
    ]
