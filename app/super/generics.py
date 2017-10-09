"""."""
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, \
    UpdateView, \
    CreateView,\
    DetailView, \
    TemplateView, \
    DeleteView, FormView
from . import mixins


class DokumenListView(
        mixins.MenuMixin, SuccessMessageMixin,
        ListView):
    """."""


class DokumenCreateView(
        mixins.MenuMixin, SuccessMessageMixin,
        mixins.SuperPermissionsMixin, CreateView):
    """."""

    pass


class DokumenUpdateView(
        mixins.MenuMixin, SuccessMessageMixin,
        mixins.SuperPermissionsMixin, UpdateView):
    """."""

    slug_url_kwarg = "id"
    pk_url_kwarg = "id"


class DokumenUpdatePasswordView(
        mixins.MenuMixin, SuccessMessageMixin,
        UpdateView):
    """."""

    slug_url_kwarg = "id"
    pk_url_kwarg = "id"


class DokumenDeleteView(
        mixins.MenuMixin, SuccessMessageMixin,
        mixins.SuperPermissionsMixin, DeleteView):
    """."""

    slug_url_kwarg = "id"
    pk_url_kwarg = "id"


class DokumenTemplateView(
        mixins.MenuMixin, SuccessMessageMixin,
        mixins.SuperPermissionsMixin, TemplateView):
    """."""

    pass


class DokumenDetailView(
        mixins.MenuMixin, SuccessMessageMixin,
        DetailView):
    """."""

    slug_url_kwarg = "id"
    pk_url_kwarg = "id"


class DokumenFormView(
    mixins.MenuMixin, SuccessMessageMixin,
        mixins.SuperPermissionsMixin, FormView):
    """."""

    pass
