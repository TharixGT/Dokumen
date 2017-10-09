"""Util."""
# coding: utf-8

from app.common.models import Carpeta


def get_folder(self):
    """Get folder.

    Returns:
        TYPE: Description
    """
    try:
        padres = Carpeta.objects.filter(padre=self)
        child = []
        for carpeta in padres.iterator():
            child.append(carpeta.id)
            child = child + children_folder(carpeta.id)
        return child
    except Exception:
        return ''


def children_folder(self):
    """Get children with folder.

    Returns:
        TYPE: Description
    """
    child = []
    child_data = Carpeta.objects.filter(
        padre__id=self).order_by('created')
    for children in child_data.iterator():
        child.append(children.id)
        child1 = children_folder(children.id)
        child = child + child1
    return child
