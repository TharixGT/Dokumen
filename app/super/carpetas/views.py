"""Coupons CRUD."""

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app.common.models import Carpeta
from . import forms
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from app.common.utils import get_deleted_objects


class CarpetaListView(ListView):
    """carpeta List View."""

    template_name = 'carpeta/list.html'
    model = Carpeta
    context_object_name = 'carpetas'

    def get_queryset(self):
        """Filter by type and customer."""
        queryset = super(CarpetaListView, self).get_queryset()
        queryset = queryset.filter()
        return queryset


class CarpetaNewView(CreateView):
    """Carpeta Create View."""

    template_name = 'carpeta/create.html'
    model = Carpeta
    form_class = forms.CarpetaForm
    success_url = reverse_lazy('super:carpeta-list')

    def get_context_data(self, **kwargs):   # noqa
        context = super(CarpetaNewView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.save()

        return super(CarpetaNewView, self).form_valid(form)

    def get_success_url(self):
        """."""
        messages.add_message(
            self.request, messages.SUCCESS,
            _("Creacion exito"))
        if 'save-and-add' in self.request.POST:
            return reverse('super:carpeta-new')
        else:
            return reverse('super:carpeta-edit', args=[self.object.id, ])

    def form_invalid(self, form):
        """."""
        messages.add_message(
            self.request, messages.ERROR,
            _("Please correct the error below."))
        return self.render_to_response(self.get_context_data(form=form))


class CarpetaUpdateView(UpdateView):
    """."""

    template_name = 'carpeta/edit.html'
    model = Carpeta
    form_class = forms.CarpetaForm
    pk_url_kwarg = 'id'
    context_object_name = 'carpetas'

    def get_queryset(self):
        """Filter by type and customer."""
        queryset = super(CarpetaUpdateView, self).get_queryset()
        return queryset

    def get_context_data(self, **kwargs):   # noqa
        context = super(CarpetaUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.save()

        return super(CarpetaUpdateView, self).form_valid(form)

    def get_success_url(self):
        """."""
        messages.add_message(
            self.request, messages.SUCCESS,
            _("Actualizacion exitosa."))
        if 'save-and-add' in self.request.POST:
            return reverse('super:carpeta-new')
        else:
            return reverse('super:carpeta-edit', args=[self.object.id, ])

    def form_invalid(self, form):
        """."""
        messages.add_message(
            self.request, messages.ERROR,
            _("Please correct the error below."))
        return self.render_to_response(self.get_context_data(form=form))


class CarpetaDeleteView(DeleteView):
    """."""

    template_name = 'carpeta/delete.html'
    model = Carpeta
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        """Judge Delete."""
        context = super(CarpetaDeleteView, self).get_context_data(**kwargs)  # noqa
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
        queryset = super(CarpetaDeleteView, self).get_queryset()
        return queryset

    def get_success_url(self):
        """."""
        messages.add_message(
            self.request, messages.SUCCESS,
            _("Eliminacion exitosa"))
        return reverse('super:carpeta-list')
