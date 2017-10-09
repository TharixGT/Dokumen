# -*- coding: utf-8 -*-
""".

Attributes:
    User (TYPE): Description
"""
from django import forms
from django.contrib.auth import get_user_model
from app.common.models import Carpeta
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
User = get_user_model()


class FolderForm(forms.ModelForm):
    """New Category form.

    Attributes:
        helper (TYPE): Description
    """

    helper = FormHelper()
    helper.method = 'POST'
    helper.form_tag = False
    helper.layout = Layout(
        Div(
            'titulo',
            css_class='col-md-6',
            style="",
        ),
        Div(
            'padre',
            css_class='col-md-6'
        ),
        Div(
            'etiqueta',
            css_class='col-md-12'
        ),
        Div(
            'color',
            css_class='col-md-6'
        ),
        Div(
            'icono',
            css_class='col-md-6'
        ),

    )

    class Meta:
        """Meta.

        Attributes:
            exclude (list): Description
            model (TYPE): Description
        """

        model = Carpeta
        exclude = []

    def __init__(self, *args, **kwargs):
        """init.

        Args:
            *args: Description
            **kwargs: Description
        """
        super(FolderForm, self).__init__(*args, **kwargs)
