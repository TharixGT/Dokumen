"""Viws."""
from app.accounts.models import User
from django.views.generic import ListView
from app.common.models import Carpeta, Archivo

from . import generics


class HomeView(generics.KualitteTemplateView):
    """HomeView.

    Attributes:
        template_name (str): Description
        user_types (TYPE): Description
    """

    user_types = [User.ADMIN, User.USER]
    template_name = 'super/home.html'

    def get_context_data(self, **kwargs):   # noqa
        context = super(HomeView, self).get_context_data(**kwargs)
        parents = Carpeta.objects.filter()
        context.update({
            'carpetasMenu': parents,
        })
        return context


class CarpetaListView(ListView):
    """carpeta List View."""

    template_name = 'super/home.html'
    model = Carpeta
    context_object_name = 'carpetasMenu'

    def get_queryset(self):
        """Filter by type and customer."""
        queryset = super(CarpetaListView, self).get_queryset()
        queryset = queryset.filter()
        return queryset


class CarpetaArchivoListView(ListView):
    """CarpetaArchivoListView List View."""

    template_name = 'super/view.html'
    model = Archivo
    context_object_name = 'archivos'

    def get_queryset(self):
        """Filter by type and customer."""
        queryset = super(CarpetaArchivoListView, self).get_queryset()
        queryset = queryset.filter(carpetas=self.kwargs['carpeta'])
        return queryset

    def get_context_data(self, **kwargs):   # noqa
        context = super(
            CarpetaArchivoListView, self).get_context_data(**kwargs)
        parents = Carpeta.objects.filter()
        context.update({
            'carpetasMenu': parents,
        })
        return context
