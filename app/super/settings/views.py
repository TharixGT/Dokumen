"""Coupons CRUD."""

from app.super.generics import DokumenUpdateView
from app.common.models import Configuracion
from . import forms
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse


class SettingsUpdateView(DokumenUpdateView):
    """."""

    template_name = 'settings/edit.html'
    model = Configuracion
    form_class = forms.SettingsForm
    pk_url_kwarg = 'id'

    def get_queryset(self):
        """get_queryset."""
        queryset = super(SettingsUpdateView, self).get_queryset()
        return queryset

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.save()

        return super(SettingsUpdateView, self).form_valid(form)

    def get_success_url(self):
        """get_success_url."""
        messages.add_message(
            self.request, messages.SUCCESS,
            _("Successful update"))
        return reverse('super:home')

    def form_invalid(self, form):
        """form_invalid."""
        messages.add_message(
            self.request, messages.ERROR,
            _("Please correct the error below."))
        return self.render_to_response(self.get_context_data(form=form))
