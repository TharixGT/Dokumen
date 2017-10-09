"""Coupons CRUD."""

from app.super.generics import DokumenListView, DokumenCreateView, \
    DokumenUpdateView, DokumenDeleteView
from app.common.models import Archivo, Carpeta
from . import forms
from app.super.mixins import SuperPermissionsMixin
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from app.common.utils import get_deleted_objects
from django.views.decorators.cache import never_cache
from django.db.models import Q
from app.super.util import get_folder
from app.accounts.models import User, Role


class FileListView(SuperPermissionsMixin, DokumenListView):
    """Archivo List View."""

    template_name = 'file/list.html'
    model = Archivo
    context_object_name = 'file_data'
    ordering = ['nombre', 'id']
    paginate_by = 10
    user_types = [User.ADMIN, User.MANAGER]

    def get_queryset(self):
        """Filter by type and customer."""
        queryset = super(FileListView, self).get_queryset()
        queryset = queryset.filter()
        return queryset


class FileNewView(DokumenCreateView):
    """Archivo Create View."""

    template_name = 'file/create.html'
    model = Archivo
    form_class = forms.FileForm
    success_url = reverse_lazy('super:file-list')
    user_types = [User.ADMIN, User.MANAGER]

    def get_form(self, *args, **kwargs):
        """."""
        form = super(FileNewView, self).get_form(*args, **kwargs)
        list_folder = get_folder(None)
        try:
            folder_exclud = Role.objects.filter(
                id=self.request.user.role.id).values_list('folder', flat=True)
            form.fields['carpetas'].queryset = Carpeta.objects.exclude(
                id__in=folder_exclud).filter(
                id__in=list_folder).order_by('modified')
        except Exception:
            form.fields['carpetas'].queryset = Carpeta.objects.filter(
                id__in=list_folder).order_by('modified')
        return form

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        form.instance.created_by = self.request.user
        form.instance.modified_by = self.request.user
        self.object.save()

        return super(FileNewView, self).form_valid(form)

    def get_success_url(self):
        """."""
        messages.add_message(
            self.request, messages.SUCCESS,
            _("Successful creation"))
        if 'save-and-add' in self.request.POST:
            return reverse('super:file-new')
        else:
            return reverse('super:file-edit', args=[self.object.id, ])

    def form_invalid(self, form):
        """."""
        messages.add_message(
            self.request, messages.ERROR,
            _("Please correct the error below."))
        return self.render_to_response(self.get_context_data(form=form))


class FileUpdateView(DokumenUpdateView):
    """."""

    template_name = 'file/edit.html'
    model = Archivo
    form_class = forms.FileForm
    pk_url_kwarg = 'id'
    user_types = [User.ADMIN, User.MANAGER]

    def get_form(self, *args, **kwargs):
        """."""
        form = super(FileUpdateView, self).get_form(*args, **kwargs)
        list_folder = get_folder(None)
        try:
            folder_exclud = Role.objects.filter(
                id=self.request.user.role.id).values_list('folder', flat=True)
            form.fields['carpetas'].queryset = Carpeta.objects.exclude(
                id__in=folder_exclud).filter(
                id__in=list_folder).order_by('modified')
        except Exception:
            form.fields['carpetas'].queryset = Carpeta.objects.filter(
                id__in=list_folder).order_by('modified')
        return form

    def get_queryset(self):
        """Filter by type and customer."""
        queryset = super(FileUpdateView, self).get_queryset()
        return queryset

    def get_context_data(self, **kwargs):   # noqa
        context = super(FileUpdateView, self).get_context_data(**kwargs)
        dataarchivo = Archivo.objects.get(id=self.object.id)
        context.update({
            'data_file_view': dataarchivo,
        })
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        form.instance.modified_by = self.request.user
        self.object.save()

        return super(FileUpdateView, self).form_valid(form)

    def get_success_url(self):
        """."""
        messages.add_message(
            self.request, messages.SUCCESS,
            _("Successful update"))
        if 'save-and-add' in self.request.POST:
            return reverse('super:file-new')
        else:
            return reverse('super:file-edit', args=[self.object.id, ])

    def form_invalid(self, form):
        """."""
        messages.add_message(
            self.request, messages.ERROR,
            _("Please correct the error below."))
        return self.render_to_response(self.get_context_data(form=form))


class FileDeleteView(DokumenDeleteView):
    """."""

    template_name = 'file/delete.html'
    model = Archivo
    pk_url_kwarg = 'id'
    user_types = [User.ADMIN, User.MANAGER]

    def get_context_data(self, **kwargs):
        """Judge Delete."""
        context = super(FileDeleteView, self).get_context_data(**kwargs)  # noqa
        #
        deletable_objects, model_count, protected = get_deleted_objects([self.object])  # noqa
        #
        context['deletable_objects'] = deletable_objects
        context['model_count'] = dict(model_count).items()
        context['protected'] = protected
        #
        return context

    def get_queryset(self):
        """Filter by type and customer."""
        queryset = super(FileDeleteView, self).get_queryset()
        return queryset

    def get_success_url(self):
        """."""
        messages.add_message(
            self.request, messages.SUCCESS,
            _("Successful delete"))
        return reverse('super:file-list')


class FileSearchView(DokumenListView):
    """FileSearchView.

    Attributes:
        context_object_name (str): Description
        queryset (TYPE): Description
        template_name (str): Description
    """

    template_name = 'file/list.html'
    queryset = Archivo.objects.all()
    context_object_name = 'file_data'
    user_types = [User.ADMIN, User.MANAGER]

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
        return super(FileSearchView, self).get(request, args, kwargs)

    def get_queryset(self):
        """get_queryset.

        Returns:
            TYPE: Description
        """
        queryset = super(FileSearchView, self).get_queryset()
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
        context = super(FileSearchView, self).get_context_data(**kwargs)
        context.update({
            'search_text': self.request.GET.get('search', None)
        })
        return context
