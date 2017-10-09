""".

Attributes:
    register (TYPE): Description
"""
from django import template
from app.accounts.models import Role
from app.common.models import Carpeta
register = template.Library()


@register.inclusion_tag('super/sub_carpeta.html')
def sub_carpetas(carpetaid, carpetasTitulo, arrayTitulo, idRole):  # noqa
    """sub_carpetas

    Args:
        carpetaid (TYPE): Description
        carpetasTitulo (TYPE): Description
        arrayTitulo (TYPE): Description
        idRole (TYPE): Description

    Returns:
        TYPE: Description
    """
    try:
        folder_exclud = Role.objects.filter(
            id=idRole).values_list('folder', flat=True)
        subs = Carpeta.objects.exclude(
            id__in=folder_exclud).filter(
            padre__id=carpetaid.id).order_by('modified')
    except Exception:
        subs = Carpeta.objects.filter(
            padre__id=carpetaid.id).order_by('modified')
    return {
        'subs': subs,
        'carpetasTitulo': carpetasTitulo,
        'arrayTitulo': arrayTitulo,
        'idRole': idRole}


@register.inclusion_tag('super/active_carpeta.html')
def active_carpetas(carpetaid, carpetasTitulo, arrayTitulo):  # noqa
    """active_carpetas

    Args:
        carpetaid (TYPE): Description
        carpetasTitulo (TYPE): Description
        arrayTitulo (TYPE): Description

    Returns:
        TYPE: Description
    """
    return {
        'items_menu': carpetaid.titulo,
        'arrayTitulo': arrayTitulo}


@register.inclusion_tag('super/end_carpeta.html')
def end_carpetas(carpetaid, idRole):  # noqa
    """end_carpetas

    Args:
        carpetaid (TYPE): Description
        idRole (TYPE): Description

    Returns:
        TYPE: Description
    """
    try:
        folder_exclud = Role.objects.filter(
            id=idRole).values_list('folder', flat=True)

        subs = Carpeta.objects.exclude(
            id__in=folder_exclud).filter(
            padre__id=carpetaid.id).order_by('modified')
    except Exception:
        subs = Carpeta.objects.filter(
            padre__id=carpetaid.id).order_by('modified')
    if subs.count() > 0:
        end = False
    else:
        end = True
    return {'subend': end, 'id': carpetaid.id, 'idRole': idRole}


@register.inclusion_tag('folder/chil_carpeta.html')
def chil_carpetas(carpetaid, idRole):  # noqa
    """chil_carpetas

    Args:
        carpetaid (TYPE): Description
        idRole (TYPE): Description

    Returns:
        TYPE: Description
    """
    try:
        folder_exclud = Role.objects.filter(
            id=idRole).values_list('folder', flat=True)

        subs = Carpeta.objects.exclude(
            id__in=folder_exclud).filter(
            padre__id=carpetaid.id).order_by('modified')
    except Exception:
        subs = Carpeta.objects.filter(
            padre__id=carpetaid.id).order_by('modified')
    return {'subs': subs, 'idRole': idRole}
