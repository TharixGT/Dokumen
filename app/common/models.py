"""model."""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.utils.translation import ugettext_lazy as _
from colorfield.fields import ColorField
from django.db import models
from django.conf import settings


class Auditable(models.Model):
    """.

    Attributes:
        created_by (TYPE): Description
        created_on (TYPE): Description
        modified_by (TYPE): Description
        modified_on (TYPE): Description
    """

    created_on = models.DateTimeField(
        auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='created_by')

    modified_on = models.DateTimeField(
        auto_now=True)
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='modified_by')

    class Meta:
        """.

        Attributes:
            abstract (bool): Description
        """

        abstract = True


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
        max_length=255, null=False,
        blank=False, verbose_name=_('Name'))
    padre = models.ForeignKey(
        'self', null=True, blank=True, verbose_name=_('Parent'))
    etiqueta = models.CharField(
        max_length=250,
        null=True, blank=True, verbose_name=_('Tag'))
    color = ColorField(
        null=True, blank=True, default='#DCDCDC', verbose_name=_('Color'))
    icono = models.CharField(
        max_length=25, null=True, blank=True,
        verbose_name=_('Icon'), default='folder')

    class Meta:
        """Meta.

        Attributes:
            db_table (str): Description
            default_related_name (str): Description
            verbose_name (TYPE): Description
            verbose_name_plural (TYPE): Description

        """

        verbose_name = _('Folder')
        verbose_name_plural = _('Folders')
        default_related_name = 'carpeta'
        db_table = 'carpetas'

    def __unicode__(self):
        """Unicode.

        Returns:
            TYPE: Description
        """
        return str(self.titulo)

    @property
    def total_archivos(self):
        """Return total auctions on GroupAuction.

        Returns:
            int: Total auction on GroupAuction
        """
        return Archivo.objects.filter(carpetas__id=self.id).count()


class Archivo(Auditable):
    """Archivo.

    Attributes:
        archivo (TYPE): Description
        carpetas (TYPE): Description
        etiqueta (TYPE): Description
        id (TYPE): Description
        nombre (TYPE): Description

    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(
        max_length=255, null=False,
        blank=False, verbose_name=_('Name'))
    etiqueta = models.CharField(
        max_length=250, null=True, blank=True,
        verbose_name=_('Tag'))
    carpetas = models.ForeignKey(
        'Carpeta', null=False, blank=False,
        verbose_name=_('Folder'))
    archivo = models.FileField(
        null=False, blank=False, upload_to='archivo/%Y/%m/%d/',
        verbose_name=_('File'))

    class Meta:
        """Meta.

        Attributes:
            db_table (str): Description
            default_related_name (str): Description
            verbose_name (TYPE): Description
            verbose_name_plural (TYPE): Description

        """

        verbose_name = _('File')
        verbose_name_plural = _('Files')
        default_related_name = 'archivo'
        db_table = 'archivos'

    def __unicode__(self):
        """Unicode.

        Returns:
            TYPE: Description
        """
        return str(self.nombre)


class Configuracion(ManejadorDocumentosBaseModel):
    """Configuracion.

    Attributes:
        archivo (TYPE): Description
        carpetas (TYPE): Description
        etiqueta (TYPE): Description
        id (TYPE): Description
        nombre (TYPE): Description

    """

    name = models.CharField(
        max_length=255,
        null=False, blank=False, verbose_name=_('Name'))
    logo = models.ImageField(
        null=False, blank=False,
        upload_to='configuracion/%Y/%m/%d/',
        verbose_name=_('Logo'))
    white_logo = models.ImageField(
        null=False, blank=False,
        upload_to='configuracion/%Y/%m/%d/',
        verbose_name=_('White logo'))
    help_file = models.FileField(
        null=True, blank=True,
        upload_to='configuracion/%Y/%m/%d/',
        verbose_name=_('Help file'))

    class Meta:
        """Meta.

        Attributes:
            db_table (str): Description
            default_related_name (str): Description
            verbose_name (TYPE): Description
            verbose_name_plural (TYPE): Description

        """

        verbose_name = _('Setting')
        verbose_name_plural = _('Settings')
        default_related_name = 'configuracion'
        db_table = 'configuracion'

    def __unicode__(self):
        """Unicode.

        Returns:
            TYPE: Description
        """
        return str(self.name)


class Link(ManejadorDocumentosBaseModel):
    """Carpeta.

    Stores a single blog entry, related to :model:`blog.Blog` and
    :model:`auth.User`.

    Attributes:
        color (TYPE): Description
        etiqueta (TYPE): Description
        icono (TYPE): Description
        id (TYPE): Description
        padre (TYPE): Description
        titulo (TYPE): Description
    """

    name = models.CharField(
        max_length=255, null=False,
        blank=False, verbose_name=_('Name'))
    url_link = models.URLField(
        null=True, blank=True, verbose_name=_('URL link'))
    color = ColorField(
        null=True, blank=True, default='#BAA130', verbose_name=_('Color'))
    icon = models.CharField(
        max_length=25, null=True, blank=True,
        verbose_name=_('Icon'), default='link')

    class Meta:
        """Meta.

        Attributes:
            db_table (str): Description
            default_related_name (str): Description
            verbose_name (TYPE): Description
            verbose_name_plural (TYPE): Description

        """

        verbose_name = _('Link')
        verbose_name_plural = _('Links')
        default_related_name = 'link'
        db_table = 'link'

    def __unicode__(self):
        """Unicode.

        Returns:
            TYPE: Description
        """
        return str(self.name)
