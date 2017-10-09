# -*- coding: utf-8 -*-
"""Forms.

Attributes:
    User (TYPE): Description
"""
# coding=utf-8

from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import Div
from allauth.account.forms import LoginForm, \
    ChangePasswordForm, ResetPasswordForm, PasswordField, \
    SetPasswordField
from allauth.account.forms import ResetPasswordKeyForm
User = get_user_model()


class CustomLoginForm(LoginForm):
    """Custom login form.

    Attributes:
        helper (TYPE): Description
    """

    password = PasswordField(label="contraseña")
    login = forms.CharField(required=True, label="Correo electrónico")
    helper = FormHelper()
    helper.form_tag = False

    def __init__(self, *args, **kwargs):
        """Custom login form.

        Args:
            *args (TYPE): Description
            **kwargs (TYPE): Description
        """
        super(CustomLoginForm, self).__init__(*args, **kwargs)


class CustomResetPasswordForm(ResetPasswordForm):
    """Reset Password Form.

    Attributes:
        helper (TYPE): Description
    """

    helper = FormHelper()
    helper.form_tag = False

    def __init__(self, *args, **kwargs):
        """Reset Password Form.

        Args:
            *args (TYPE): Description
            **kwargs (TYPE): Description
        """
        super(CustomResetPasswordForm, self).__init__(*args, **kwargs)


class CustomResetPasswordKeyForm(ResetPasswordKeyForm):
    """Reset Password with Key Form.

    Attributes:
        helper (TYPE): Description
    """

    password1 = SetPasswordField(label="Nueva contraseña")
    password2 = PasswordField(label="Nueva contraseña ( Otra vez)")
    helper = FormHelper()
    helper.form_tag = False

    def __init__(self, *args, **kwargs):
        """Reset Password with Key Form.

        Args:
            *args (TYPE): Description
            **kwargs (TYPE): Description
        """
        super(CustomResetPasswordKeyForm, self).__init__(*args, **kwargs)


class CustomChangePasswordForm(ChangePasswordForm):
    """Change Password Form.

    Attributes:
        helper (TYPE): Description
    """

    helper = FormHelper()
    helper.form_tag = False

    def __init__(self, *args, **kwargs):
        """Change Password Form.

        Args:
            *args (TYPE): Description
            **kwargs (TYPE): Description
        """
        super(CustomChangePasswordForm, self).__init__(*args, **kwargs)


class EditProfileForm(ModelForm):
    """Edit Profile Form.

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
            Div('first_name', css_class='col-md-6'),
            Div('last_name', css_class='col-md-6'),
            Div('email', css_class='col-md-6'),
        ),
    )

    def __init__(self, *args, **kwargs):
        """Edit profile form.

        Args:
            *args (TYPE): Description
            **kwargs (TYPE): Description
        """
        super(EditProfileForm, self).__init__(*args, **kwargs)

    class Meta:
        """Meta class for Edit Profile.

        Attributes:
            exclude (list): Description
            model (TYPE): Description
        """

        model = User
        exclude = [
            'password',
            'last_login',
            'is_superuser',
            'is_active',
            'email',
            'user_type']
