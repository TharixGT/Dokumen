"""Forms.

Attributes:
    User (TYPE): Description
"""
# coding=utf-8

from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import Div
from allauth.account.forms import LoginForm, SignupForm, \
    ChangePasswordForm, ResetPasswordForm
from allauth.account.forms import ResetPasswordKeyForm
User = get_user_model()


class CustomLoginForm(LoginForm):
    """Custom login form.

    Attributes:
        helper (TYPE): Description
    """

    helper = FormHelper()
    helper.form_tag = False

    def __init__(self, *args, **kwargs):
        """Custom login form.

        Args:
            *args (TYPE): Description
            **kwargs (TYPE): Description
        """
        super(CustomLoginForm, self).__init__(*args, **kwargs)


class CustomSignupForm(SignupForm):
    """Custom login form.

    Attributes:
        first_name (TYPE): Description
        helper (TYPE): Description
        last_name (TYPE): Description
    """

    first_name = forms.CharField(
        max_length=50, label=_('First name'),
        widget=forms.TextInput(attrs={'placeholder': _('First name')})
    )
    last_name = forms.CharField(
        max_length=50, label=_('Last name'),
        widget=forms.TextInput(attrs={'placeholder': _('Last name')})
    )

    helper = FormHelper()
    helper.html5_required = True
    helper.form_tag = False
    helper.layout = Layout(
        Div(
            'email',
            'password1',
            'password2',
            css_class='col-md-4',

        ),
        Div(
            'first_name',
            'last_name',
            css_class='col-md-4',
        ),
    )

    def __init__(self, *args, **kwargs):
        """Custom login form.

        Args:
            *args (TYPE): Description
            **kwargs (TYPE): Description
        """
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'autofocus': 'autofocus'})

    def custom_signup(self, request, user):
        """Custom login form.

        Args:
            request (TYPE): Description
            user (TYPE): Description
        """
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_active = True
        user.user_type = User.USER
        user.save()


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
