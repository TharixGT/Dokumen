"""Viws."""
from app.accounts.models import User
from app.common.models import Carpeta, Archivo
from django.views.decorators.cache import never_cache
from . import generics
from django.db.models import Q
from django.conf import settings


class HomeView(generics.DokumenTemplateView):
    """HomeView.

    Attributes:
        template_name (str): Description
        user_types (TYPE): Description
    """

    user_types = [User.ADMIN, User.USER, User.MANAGER]
    template_name = 'super/home.html'


class FolderListView(generics.DokumenListView):
    """carpeta List View.

    Attributes:
        context_object_name (str): Description
        model (TYPE): Description
        template_name (str): Description
    """

    template_name = 'super/home.html'
    model = Carpeta
    context_object_name = 'carpetasMenu'

    def get_queryset(self):
        """Filter by type and customer.

        Returns:
            TYPE: Description
        """
        queryset = super(FolderListView, self).get_queryset()
        queryset = queryset.filter()
        return queryset


class CarpetaArchivoListView(generics.DokumenListView):
    """CarpetaArchivoListView List View.

    Attributes:
        context_object_name (str): Description
        model (TYPE): Description
        template_name (str): Description
    """

    template_name = 'super/view.html'
    model = Archivo
    context_object_name = 'archivos'
    ordering = ['nombre', 'id']
    paginate_by = 10

    def get_queryset(self):
        """Filter by type and customer.

        Returns:
            TYPE: Description
        """
        queryset = super(CarpetaArchivoListView, self).get_queryset()
        queryset = queryset.filter(carpetas=self.kwargs['carpeta'])
        return queryset

    def get_context_data(self, **kwargs):   # noqa
        """Summary

        Args:
            **kwargs: Description

        Returns:
            TYPE: Description
        """
        context = super(
            CarpetaArchivoListView, self).get_context_data(**kwargs)
        items_menu = []
        parents = Carpeta.objects.get(id=self.kwargs['carpeta'])
        carpetaid = Carpeta.objects.get(id=parents.id)
        items_menu.append(carpetaid.titulo)
        while carpetaid.padre is not None:
            items_menu.append(carpetaid.padre.titulo)
            carpetaid = Carpeta.objects.get(id=carpetaid.padre.id)
        context.update({
            'carpetasTitulo': parents.titulo,
            'arrayTitulo': items_menu,
            'carpetasColor': parents.color,
            'id_carpeta': self.kwargs['carpeta'],

        })
        return context


class SearchView(generics.DokumenListView):
    """SearchView.

    Attributes:
        context_object_name (str): Description
        queryset (TYPE): Description
        template_name (str): Description
    """

    template_name = 'super/results.html'
    queryset = Archivo.objects.all()
    context_object_name = 'results'
    paginate_by = 10

    @never_cache
    def get(self, request, *args, **kwargs):
        """get.

        Args:
            request (TYPE): Description
            *args: Description
            **kwargs: Description

        Returns:
            TYPE: Description
        """
        return super(SearchView, self).get(request, args, kwargs)

    def get_queryset(self):
        """get_queryset.

        Returns:
            TYPE: Description
        """
        queryset = super(SearchView, self).get_queryset()
        search_text = self.request.GET.get('search', None)
        if search_text:
            try:
                queryset = queryset.filter(
                    Q(nombre__icontains=search_text) |
                    Q(etiqueta__icontains=search_text) |
                    Q(carpetas__titulo__icontains=search_text) |
                    Q(modified_on__year=search_text) |
                    Q(modified_on__month=search_text) |
                    Q(modified_on__day=search_text))
            except ValueError:
                queryset = queryset.filter(
                    Q(nombre__icontains=search_text) |
                    Q(etiqueta__icontains=search_text) |
                    Q(carpetas__titulo__icontains=search_text))
        return queryset.order_by('nombre')

    def get_context_data(self, **kwargs):   # noqa
        """get_context_data.

        Args:
            **kwargs: Description

        Returns:
            TYPE: Description
        """
        context = super(SearchView, self).get_context_data(**kwargs)
        context.update({
            'search_text': self.request.GET.get('search', None)
        })
        return context


class CarpetaSearchListView(generics.DokumenListView):
    """CarpetaSearchListView.

    Attributes:
        context_object_name (str): Description
        queryset (TYPE): Description
        template_name (str): Description
    """

    template_name = 'super/view.html'
    queryset = Archivo.objects.all()
    context_object_name = 'archivos'
    paginate_by = 10

    @never_cache
    def get(self, request, *args, **kwargs):
        """get.

        Args:
            request (TYPE): Description
            *args: Description
            **kwargs: Description

        Returns:
            TYPE: Description
        """
        return super(CarpetaSearchListView, self).get(request, args, kwargs)

    def get_queryset(self):
        """get_queryset.

        Returns:
            TYPE: Description
        """
        queryset = super(CarpetaSearchListView, self).get_queryset()
        queryset = queryset.filter(carpetas=self.kwargs['carpeta'])
        search_text = self.request.GET.get('search', None)
        if search_text:
            try:
                queryset = queryset.filter(
                    Q(nombre__icontains=search_text) |
                    Q(etiqueta__icontains=search_text) |
                    Q(carpetas__titulo__icontains=search_text) |
                    Q(modified_on__year=search_text) |
                    Q(modified_on__month=search_text) |
                    Q(modified_on__day=search_text))
            except ValueError:
                queryset = queryset.filter(
                    Q(nombre__icontains=search_text) |
                    Q(etiqueta__icontains=search_text) |
                    Q(carpetas__titulo__icontains=search_text))
        return queryset.order_by('nombre')

    def get_context_data(self, **kwargs):   # noqa
        """get_context_data.

        Args:
            **kwargs: Description

        Returns:
            TYPE: Description
        """
        context = super(CarpetaSearchListView, self).get_context_data(**kwargs)
        items_menu = []
        parents = Carpeta.objects.get(id=self.kwargs['carpeta'])
        carpetaid = Carpeta.objects.get(id=parents.id)
        items_menu.append(carpetaid.titulo)
        while carpetaid.padre is not None:
            items_menu.append(carpetaid.padre.titulo)
            carpetaid = Carpeta.objects.get(id=carpetaid.padre.id)
        context.update({
            'carpetasTitulo': parents.titulo,
            'carpetasColor': parents.color,
            'arrayTitulo': items_menu,
            'search_text': self.request.GET.get('search', None),
            'id_carpeta': self.kwargs['carpeta'],
        })
        return context


class ViewFileView(generics.DokumenDetailView):
    """View File view."""

    template_name = 'super/view-file.html'
    model = Archivo
    context_object_name = 'archivo'
    pk_url_kwarg = 'id'
    slug_url_kwarg = 'id'

    def get_context_data(self, **kwargs):   # noqa
        context = super(ViewFileView, self).get_context_data(**kwargs)
        context.update({
            'site': settings.DOMAIN
        })
        return context
