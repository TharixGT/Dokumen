# -*- coding: utf-8 -*-
"""Admin."""
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from . import models


admin.site.register(models.Carpeta)
admin.site.register(models.Archivo)
