"""model."""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.utils.translation import ugettext_lazy as _
from colorfield.fields import ColorField
from django.db import models


class ManejadorDocumentosBaseModel(models.Model):
    """ManejadorDocumentosBaseModel.

    Attributes:
        created (TYPE): Description
        modified (TYPE): Description
    """

    created = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name=_('Created'))
    modified = models.DateTimeField(
        auto_now=True, editable=False, verbose_name=_('Modify'))

    class Meta:
        """Meta.

        Attributes:
            abstract (bool): Description
        """

        abstract = True


class Carpeta(ManejadorDocumentosBaseModel):
    """Carpeta.

    Attributes:
        color (TYPE): Description
        etiqueta (TYPE): Description
        icono (TYPE): Description
        id (TYPE): Description
        padre (TYPE): Description
        titulo (TYPE): Description
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(
        max_length=75, null=False,
        blank=False, verbose_name=_('Titulo'))
    padre = models.ForeignKey('self', null=True, blank=True)
    etiqueta = models.TextField(
        null=True, blank=True, verbose_name=_('Etiquetas'))
    color = ColorField(default='#FF0000', verbose_name=_('Color'))
    icono = models.CharField(
        max_length=25, null=False,
        blank=False, verbose_name=_('Icono'))

    class Meta:
        """Meta.

        Attributes:
            db_table (str): Description
            default_related_name (str): Description
            verbose_name (TYPE): Description
            verbose_name_plural (TYPE): Description

        Deleted Attributes:
            ordering (tuple): Description
        """

        verbose_name = _('Carpeta')
        verbose_name_plural = _('Carpetas')
        default_related_name = 'carpeta'
        db_table = 'carpetas'

    def __unicode__(self):
        """Unicode.

        Returns:
            TYPE: Description
        """
        return str(self.titulo)


class Archivo(ManejadorDocumentosBaseModel):
    """Archivo.

    Attributes:
        color (TYPE): Description
        etiqueta (TYPE): Description
        icono (TYPE): Description
        id (TYPE): Description
        padre (TYPE): Description
        titulo (TYPE): Description
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(
        max_length=75, null=False,
        blank=False, verbose_name=_('Nombre'))
    etiqueta = models.TextField(
        null=True, blank=True, verbose_name=_('Etiquetas'))
    carpetas = models.ForeignKey('Carpeta', null=False, blank=False)
    archivo = models.FileField(
        _('Archivo'), null=True, blank=True, upload_to='archivo/%Y/%m/%d/')

    class Meta:
        """Meta.

        Attributes:
            db_table (str): Description
            default_related_name (str): Description
            verbose_name (TYPE): Description
            verbose_name_plural (TYPE): Description

        Deleted Attributes:
            ordering (tuple): Description
        """

        verbose_name = _('Archivo')
        verbose_name_plural = _('Archivos')
        default_related_name = 'archivo'
        db_table = 'archivos'

    def __unicode__(self):
        """Unicode.

        Returns:
            TYPE: Description
        """
        return str(self.nombre)
