"""View."""
from allauth.account.views import PasswordChangeView, LogoutView, LoginView, \
    PasswordResetView, PasswordResetDoneView, AccountInactiveView, \
    EmailVerificationSentView, PasswordResetFromKeyView, \
    PasswordResetFromKeyDoneView, EmailView, ConfirmEmailView
from django.contrib.auth.decorators import login_required
from app.super import mixins


class CustomPasswordChangeView(mixins.MenuMixin, PasswordChangeView):
    """CustomPasswordChangeView."""

custom_password_change = login_required(CustomPasswordChangeView.as_view())


class CustomLogoutView(mixins.MenuMixin, LogoutView):
    """CustomLogoutView."""

custom_logout = login_required(CustomLogoutView.as_view())


class CustomLoginView(mixins.SettingsMixin, LoginView):
    """CustomLoginView."""

custom_login = CustomLoginView.as_view()


class CustomPasswordResetView(mixins.SettingsMixin, PasswordResetView):
    """CustomPasswordResetView."""

custom_password_reset = CustomPasswordResetView.as_view()


class CustomPasswordResetDoneView(mixins.SettingsMixin, PasswordResetDoneView):
    """CustomPasswordResetDoneView."""

custom_password_reset_done = CustomPasswordResetDoneView.as_view()


class CustomInactiveView(mixins.SettingsMixin, AccountInactiveView):
    """CustomInactiveView."""

custom_inactive = CustomInactiveView.as_view()


class CustomEmailVerificationSentViewView(
        mixins.SettingsMixin, EmailVerificationSentView):
    """CustomEmailVerificationSentViewView."""

custom_inactive = CustomEmailVerificationSentViewView.as_view()


class CustomPasswordResetFromKeyViewViewView(
        mixins.SettingsMixin, PasswordResetFromKeyView):
    """CustomPasswordResetFromKeyViewViewView."""

custom_password_reset_from_key = CustomPasswordResetFromKeyViewViewView.as_view()


class CustomPasswordResetFromKeyDoneView(
        mixins.SettingsMixin, PasswordResetFromKeyDoneView):
    """CustomPasswordResetFromKeyDoneView."""

custom_password_reset_from_key_done = CustomPasswordResetFromKeyDoneView.as_view()


class CustomEmailView(mixins.SettingsMixin, EmailView):
    """CustomEmailView."""

custom_email = login_required(CustomEmailView.as_view())


class CustomEmailVerificationSentView(
        mixins.SettingsMixin, EmailVerificationSentView):
    """CustomEmailVerificationSentView."""

custom_email_verification_sent = CustomEmailVerificationSentView.as_view()


class CustomConfirmEmailView(mixins.SettingsMixin, ConfirmEmailView):
    """CustomConfirmEmailView."""

custom_confirm_email = login_required(CustomConfirmEmailView.as_view())
