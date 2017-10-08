from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, \
    UpdateView, \
    CreateView,\
    DetailView, \
    TemplateView, \
    DeleteView
from . import mixins


class KualitteListView(
        SuccessMessageMixin,
        mixins.SuperPermissionsMixin, ListView):
    pass


class KualitteCreateView(
        SuccessMessageMixin,
        mixins.SuperPermissionsMixin, CreateView):
    pass


class KualitteUpdateView(
        SuccessMessageMixin,
        mixins.SuperPermissionsMixin, UpdateView):
    slug_url_kwarg = "id"
    pk_url_kwarg = "id"


class KualitteDeleteView(
        SuccessMessageMixin,
        mixins.SuperPermissionsMixin, DeleteView):
    slug_url_kwarg = "id"
    pk_url_kwarg = "id"


class KualitteTemplateView(
        SuccessMessageMixin,
        mixins.SuperPermissionsMixin, TemplateView):
    pass


class KualitteDetailView(
        SuccessMessageMixin,
        mixins.SuperPermissionsMixin, DetailView):
    slug_url_kwarg = "id"
    pk_url_kwarg = "id"


class KualitteNotarioDetailView(
        SuccessMessageMixin,
        mixins.NotaryOrSuperPermissionsMixin, DetailView):
    slug_url_kwarg = "id"
    pk_url_kwarg = "id"
