# -*- coding: utf-8 -*-
""".

Attributes:
    User (TYPE): Description
"""
from django import forms
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
from allauth.account.forms import SetPasswordField, PasswordField
User = get_user_model()


class UserForm(forms.ModelForm):
    """New Category form.

    Attributes:
        helper (TYPE): Description
    """

    helper = FormHelper()
    helper.method = 'POST'
    helper.form_tag = False
    helper.layout = Layout(
        Div(
            Div(
                'email',
                css_class='col-md-12',
            ),
            css_class='col-md-12',
        ),
        Div(
            Div(
                'first_name',
                css_class='col-md-6'
            ),
            Div(
                'last_name',
                css_class='col-md-6'
            ),
            css_class='col-md-12',
        ),


        Div(
            Div(
                'user_type',
                css_class='col-md-6'
            ),
            Div(
                'role',
                css_class='col-md-6'
            ),
            css_class='col-md-12',
        ),


        Div(
            Div(
                'is_active',
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

        model = User
        exclude = ['password', 'repeat_password']

    def __init__(self, *args, **kwargs):
        """init.

        Args:
            *args: Description
            **kwargs: Description
        """
        super(UserForm, self).__init__(*args, **kwargs)


class CustomChangePasswordForm1(forms.ModelForm):
    """Change Password Form.

    Attributes:
        helper (TYPE): Description
    """

    password = SetPasswordField(label="Contraseña")
    repeat_password = PasswordField(label="Confirmar contraseña")

    helper = FormHelper()
    helper.form_tag = False

    helper.layout = Layout(

        Div(
            'password',
            css_class='col-md-12',
            style="",
        ),
        Div(
            'repeat_password',
            css_class='col-md-12'

        ),
        Div(
            'email',
            css_class='col-md-6',
            hidden="true"
        ),
    )

    class Meta:
        """Meta.

        Attributes:
            exclude (list): Description
            model (TYPE): Description
        """

        model = User
        exclude = ['first_name', 'last_name', 'user_type', 'is_active']

    def __init__(self, *args, **kwargs):
        """."""
        super(CustomChangePasswordForm1, self).__init__(*args, **kwargs)


class NewUserForm(forms.ModelForm):
    """Custom login form.

    Attributes:
        first_name (TYPE): Description
        helper (TYPE): Description
        last_name (TYPE): Description
    """

    helper = FormHelper()
    helper.method = 'POST'
    helper.form_tag = False
    helper.layout = Layout(
        Div(
            Div(
                'email',
                css_class='col-md-12',

            ),
            css_class='col-md-12',
        ),
        Div(
            Div(
                'first_name',
                css_class='col-md-6',
            ),
            Div(
                'last_name',
                css_class='col-md-6',
            ),
            css_class='col-md-12',
        ),
        Div(
            Div(
                'user_type',
                css_class='col-md-6',

            ),
            Div(
                'role',
                css_class='col-md-6',

            ),
            css_class='col-md-12',
        ),

    )

    class Meta:
        """Meta.

        Attributes:
            exclude (list): Description
            model (TYPE): Description
        """

        model = User
        exclude = ['password']

    def __init__(self, *args, **kwargs):
        """Custom login form.

        Args:
            *args (TYPE): Description
            **kwargs (TYPE): Description
        """
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'autofocus': 'autofocus'})

    def clean_email(self):
        """Validate Email."""
        email = self.cleaned_data['email']
        if email:
            try:
                if User.objects.filter(
                        email=email).count():
                    raise forms.ValidationError(
                        'Correo electrónico ya existe, ingrese otro')
                return email
            except User.DoesNotExist:
                return email
            except Exception:
                raise forms.ValidationError(
                    'Correo electrónico ya existe, ingrese otro')
                return email
