# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-14 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, choices=[(b'user', 'User'), (b'admin', 'Admin')], max_length=5, null=True, verbose_name='Type'),
        ),
    ]
