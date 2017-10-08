"""View."""
from django.views.generic.base import TemplateResponseMixin, View
from allauth.account import app_settings
from allauth.account.adapter import get_adapter
from allauth.account.utils import perform_login, url_str_to_user_pk
from django.http import Http404
from allauth.account.models import EmailConfirmation


class ConfirmEmailView(TemplateResponseMixin, View):
    """Confirm Email View."""

    template_name = "account/email_confirm." + app_settings.TEMPLATE_EXTENSION

    def login_on_confirm(self, confirmation):
        """Login on confrim."""
        user_pk = None
        user_pk_str = get_adapter(self.request).unstash_user(self.request)
        if user_pk_str:
            user_pk = url_str_to_user_pk(user_pk_str)
        user = confirmation.email_address.user
        if user_pk == user.pk and self.request.user.is_anonymous():
            return perform_login(self.request,
                                 user,
                                 app_settings.EmailVerificationMethod.NONE,
                                 # passed as callable, as this method
                                 # depends on the authenticated state
                                 redirect_url=self.get_redirect_url)

        return None

    def get_object(self, queryset=None):
        """Get object."""
        if queryset is None:
            queryset = self.get_queryset()
        try:
            return queryset.get(key=self.kwargs["key"].lower())
        except EmailConfirmation.DoesNotExist:
            raise Http404()

    def get_queryset(self):
        """Get queryset."""
        qs = EmailConfirmation.objects.all_valid()
        qs = qs.select_related("email_address__user")
        return qs

    def get_context_data(self, **kwargs):
        """Get context data."""
        ctx = kwargs
        ctx["confirmation"] = self.object
        return ctx

    def get_redirect_url(self):
        """Get redirect url."""
        return get_adapter(self.request).get_email_confirmation_redirect_url(
            self.request)
