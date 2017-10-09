# -*- coding: utf-8 -*-
""".

Attributes:
    User (TYPE): Description
"""
from django import forms
from django.contrib.auth import get_user_model
from app.common.models import Link
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
User = get_user_model()


class LinkForm(forms.ModelForm):
    """Link form.

    Attributes:
        helper (TYPE): Description
    """

    helper = FormHelper()
    helper.method = 'POST'
    helper.form_tag = False
    helper.layout = Layout(
        Div(
            Div(
                'name',
                css_class='col-md-6',
            ),
            Div(
                'url_link',
                css_class='col-md-6'
            ),
            css_class='col-md-12',
        ),
        Div(
            Div(
                'color',
                css_class='col-md-6'
            ),
            Div(
                'icon',
                css_class='col-md-6'
            ),
            css_class='col-md-12'
        ),

    )

    class Meta:
        """Meta.

        Attributes:
            exclude (list): Description
            model (TYPE): Description
        """

        model = Link
        exclude = []

    def __init__(self, *args, **kwargs):
        """init.

        Args:
            *args: Description
            **kwargs: Description
        """
        super(LinkForm, self).__init__(*args, **kwargs)
