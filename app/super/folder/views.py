"""Coupons CRUD."""

from app.super.generics import DokumenListView, DokumenCreateView, \
    DokumenUpdateView, DokumenDeleteView
from app.common.models import Carpeta, Archivo
from . import forms
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from app.common.utils import get_deleted_objects
from app.super.mixins import SuperPermissionsMixin
from app.super.util import get_folder
from app.accounts.models import User, Role


class FolderListView(SuperPermissionsMixin, DokumenListView):
    """carpeta List View."""

    template_name = 'folder/list.html'
    model = Carpeta
    context_object_name = 'folder_data'
    user_types = [User.ADMIN, User.MANAGER]

    def get_queryset(self):
        """Filter by type and customer."""
        queryset = super(FolderListView, self).get_queryset()

        try:
            folder_exclud = Role.objects.filter(
                id=self.request.user.role.id).values_list('folder', flat=True)
            queryset = queryset.exclude(
                id__in=folder_exclud).filter(padre=None).order_by('modified')
        except Exception:
            queryset = queryset.filter(padre=None).order_by('modified')
        return queryset


class FolderNewView(DokumenCreateView):
    """Carpeta Create View."""

    template_name = 'folder/create.html'
    model = Carpeta
    form_class = forms.FolderForm
    success_url = reverse_lazy('super:folder-list')
    user_types = [User.ADMIN, User.MANAGER]

    def get_form(self, *args, **kwargs):
        """."""
        form = super(FolderNewView, self).get_form(*args, **kwargs)
        list_folder = get_folder(None)
        try:
            folder_exclud = Role.objects.filter(
                id=self.request.user.role.id).values_list('folder', flat=True)
            form.fields['padre'].queryset = Carpeta.objects.exclude(
                id__in=folder_exclud).filter(
                id__in=list_folder).order_by('modified')
        except Exception:
            form.fields['padre'].queryset = Carpeta.objects.filter(
                id__in=list_folder).order_by('modified')
        return form

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.save()

        return super(FolderNewView, self).form_valid(form)

    def get_success_url(self):
        """."""
        messages.add_message(
            self.request, messages.SUCCESS,
            _("Successful creation"))
        if 'save-and-add' in self.request.POST:
            return reverse('super:folder-new')
        else:
            return reverse('super:folder-edit', args=[self.object.id, ])

    def form_invalid(self, form):
        """."""
        messages.add_message(
            self.request, messages.ERROR,
            _("Please correct the error below."))
        return self.render_to_response(self.get_context_data(form=form))


class FolderUpdateView(DokumenUpdateView):
    """."""

    template_name = 'folder/edit.html'
    model = Carpeta
    form_class = forms.FolderForm
    pk_url_kwarg = 'id'
    user_types = [User.ADMIN, User.MANAGER]

    def get_form(self, *args, **kwargs):
        """."""
        form = super(FolderUpdateView, self).get_form(*args, **kwargs)
        list_folder = get_folder(None)
        try:
            folder_exclud = Role.objects.filter(
                id=self.request.user.role.id).values_list('folder', flat=True)
            form.fields['padre'].queryset = Carpeta.objects.exclude(
                id__in=folder_exclud).filter(
                id__in=list_folder).order_by('modified')
        except Exception:
            form.fields['padre'].queryset = Carpeta.objects.filter(
                id__in=list_folder).order_by('modified')
        return form

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.save()

        return super(FolderUpdateView, self).form_valid(form)

    def get_success_url(self):
        """."""
        messages.add_message(
            self.request, messages.SUCCESS,
            _("Successful update"))
        if 'save-and-add' in self.request.POST:
            return reverse('super:folder-new')
        else:
            return reverse('super:folder-edit', args=[self.object.id, ])

    def form_invalid(self, form):
        """."""
        messages.add_message(
            self.request, messages.ERROR,
            _("Please correct the error below."))
        return self.render_to_response(self.get_context_data(form=form))


class FolderDeleteView(DokumenDeleteView):
    """."""

    template_name = 'folder/delete.html'
    model = Carpeta
    pk_url_kwarg = 'id'
    user_types = [User.ADMIN, User.MANAGER]

    def get_context_data(self, **kwargs):
        """Judge Delete."""
        context = super(FolderDeleteView, self).get_context_data(**kwargs)  # noqa
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
        queryset = super(FolderDeleteView, self).get_queryset()
        return queryset

    def get_success_url(self):
        """."""
        messages.add_message(
            self.request, messages.SUCCESS,
            _("Successful delete"))
        return reverse('super:folder-list')


class FolderFileUpdateView(DokumenListView):
    """FolderFileUpdateView List View.

    Attributes:
        context_object_name (str): Description
        model (TYPE): Description
        template_name (str): Description
    """

    template_name = 'folder/view.html'
    model = Archivo
    context_object_name = 'archivos'
    ordering = ['nombre', 'id']
    paginate_by = 10
    user_types = [User.ADMIN, User.MANAGER]

    def get_queryset(self):
        """Filter by type and customer.

        Returns:
            TYPE: Description
        """
        queryset = super(FolderFileUpdateView, self).get_queryset()
        queryset = queryset.filter(carpetas=self.kwargs['id'])
        return queryset

    def get_context_data(self, **kwargs):   # noqa
        """Summary

        Args:
            **kwargs: Description

        Returns:
            TYPE: Description
        """
        context = super(
            FolderFileUpdateView, self).get_context_data(**kwargs)
        items_menu = []
        parents = Carpeta.objects.get(id=self.kwargs['id'])
        carpetaid = Carpeta.objects.get(id=parents.id)
        items_menu.append(carpetaid.titulo)
        while carpetaid.padre is not None:
            items_menu.append(carpetaid.padre.titulo)
            carpetaid = Carpeta.objects.get(id=carpetaid.padre.id)
        context.update({
            'carpetasTitulo': parents.titulo,
            'arrayTitulo': items_menu,
            'carpetasColor': parents.color,
            'id_carpeta': self.kwargs['id'],

        })
        return context
