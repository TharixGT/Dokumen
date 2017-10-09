# -*- coding: utf-8 -*-
""".

Attributes:
    User (TYPE): Description
"""
from django import forms
from django.contrib.auth import get_user_model
from app.common.models import Archivo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
User = get_user_model()


class FileForm(forms.ModelForm):
    """New Category form.

    Attributes:
        helper (TYPE): Description
    """

    helper = FormHelper()
    helper.method = 'POST'
    helper.form_tag = False
    helper.layout = Layout(
        Div(
            'nombre',
            css_class='col-md-6',
            style="",
        ),
        Div(
            'carpetas',
            css_class='col-md-6'
        ),
        Div(
            'etiqueta',
            css_class='col-md-12'
        ),
        Div(
            'archivo',
            css_class='col-md-12'
        ),


    )

    class Meta:
        """Meta.

        Attributes:
            exclude (list): Description
            model (TYPE): Description
        """

        model = Archivo
        exclude = ['modified_by', 'created_by']

    def __init__(self, *args, **kwargs):
        """init.

        Args:
            *args: Description
            **kwargs: Description
        """
        super(FileForm, self).__init__(*args, **kwargs)
