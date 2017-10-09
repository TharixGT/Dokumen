"""Coupons CRUD."""

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app.common.models import Archivo, Carpeta
from . import forms
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from app.common.utils import get_deleted_objects


class ArchivoListView(ListView):
    """Archivo List View."""

    template_name = 'archivo/list.html'
    model = Archivo
    context_object_name = 'archivos'

    def get_queryset(self):
        """Filter by type and customer."""
        queryset = super(ArchivoListView, self).get_queryset()
        queryset = queryset.filter()
        return queryset

    def get_context_data(self, **kwargs):   # noqa
        context = super(ArchivoListView, self).get_context_data(**kwargs)
        parents = Carpeta.objects.filter()
        context.update({
            'carpetasMenu': parents,
        })
        return context


class ArchivoNewView(CreateView):
    """Archivo Create View."""

    template_name = 'archivo/create.html'
    model = Archivo
    form_class = forms.ArchivoForm
    success_url = reverse_lazy('super:archivo-list')

    def get_context_data(self, **kwargs):   # noqa
        context = super(ArchivoNewView, self).get_context_data(**kwargs)
        parents = Carpeta.objects.filter()
        context.update({
            'carpetasMenu': parents,
        })
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.save()

        return super(ArchivoNewView, self).form_valid(form)

    def get_success_url(self):
        """."""
        messages.add_message(
            self.request, messages.SUCCESS,
            _("Creacion exito"))
        if 'save-and-add' in self.request.POST:
            return reverse('super:archivo-new')
        else:
            return reverse('super:archivo-edit', args=[self.object.id, ])

    def form_invalid(self, form):
        """."""
        messages.add_message(
            self.request, messages.ERROR,
            _("Please correct the error below."))
        return self.render_to_response(self.get_context_data(form=form))


class ArchivoUpdateView(UpdateView):
    """."""

    template_name = 'archivo/edit.html'
    model = Archivo
    form_class = forms.ArchivoForm
    pk_url_kwarg = 'id'
    context_object_name = 'Archivos'

    def get_queryset(self):
        """Filter by type and customer."""
        queryset = super(ArchivoUpdateView, self).get_queryset()
        return queryset

    def get_context_data(self, **kwargs):   # noqa
        context = super(ArchivoUpdateView, self).get_context_data(**kwargs)
        parents = Carpeta.objects.filter()
        context.update({
            'carpetasMenu': parents,
        })
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.save()

        return super(ArchivoUpdateView, self).form_valid(form)

    def get_success_url(self):
        """."""
        messages.add_message(
            self.request, messages.SUCCESS,
            _("Actualizacion exitosa."))
        if 'save-and-add' in self.request.POST:
            return reverse('super:archivo-new')
        else:
            return reverse('super:archivo-edit', args=[self.object.id, ])

    def form_invalid(self, form):
        """."""
        messages.add_message(
            self.request, messages.ERROR,
            _("Please correct the error below."))
        return self.render_to_response(self.get_context_data(form=form))


class ArchivoDeleteView(DeleteView):
    """."""

    template_name = 'archivo/delete.html'
    model = Archivo
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        """Judge Delete."""
        context = super(ArchivoDeleteView, self).get_context_data(**kwargs)  # noqa
        #
        deletable_objects, model_count, protected = get_deleted_objects([self.object])  # noqa
        #
        context['deletable_objects'] = deletable_objects
        context['model_count'] = dict(model_count).items()
        context['protected'] = protected
        #
        parents = Carpeta.objects.filter()
        context.update({
            'carpetasMenu': parents,
        })
        return context

    def get_queryset(self):
        """Filter by type and customer."""
        queryset = super(ArchivoDeleteView, self).get_queryset()
        return queryset

    def get_success_url(self):
        """."""
        messages.add_message(
            self.request, messages.SUCCESS,
            _("Eliminacion exitosa"))
        return reverse('super:archivo-list')
