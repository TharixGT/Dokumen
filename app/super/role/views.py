"""Role View."""

from app.super.generics import DokumenListView, DokumenCreateView, \
    DokumenUpdateView, DokumenDeleteView
from app.accounts.models import Role
from . import forms
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from app.common.utils import get_deleted_objects
from app.super.mixins import SuperPermissionsMixin


class RoleListView(SuperPermissionsMixin, DokumenListView):
    """Role List View.

    Attributes:
        context_object_name (str): Description
        model (TYPE): Description
        template_name (str): Description
    """

    template_name = 'role/list.html'
    model = Role
    context_object_name = 'role_data'

    def get_queryset(self):
        """Filter by type and customer.

        Returns:
            TYPE: Description
        """
        queryset = super(RoleListView, self).get_queryset()
        return queryset


class RoleNewView(DokumenCreateView):
    """role Create View.

    Attributes:
        form_class (TYPE): Description
        model (TYPE): Description
        object (TYPE): Description
        success_url (TYPE): Description
        template_name (str): Description
    """

    template_name = 'role/create.html'
    model = Role
    form_class = forms.RoleForm
    success_url = reverse_lazy('super:role-list')

    def form_valid(self, form):
        """If the form is valid, save the associated model.

        Args:
            form (TYPE): Description

        Returns:
            TYPE: Description
        """
        self.object = form.save(commit=False)
        self.object.save()

        return super(RoleNewView, self).form_valid(form)

    def get_success_url(self):
        """.

        Returns:
            TYPE: Description
        """
        messages.add_message(
            self.request, messages.SUCCESS,
            _("Successful creation"))
        if 'save-and-add' in self.request.POST:
            return reverse('super:role-new')
        else:
            return reverse('super:role-edit', args=[self.object.id, ])

    def form_invalid(self, form):
        """.

        Args:
            form (TYPE): Description

        Returns:
            TYPE: Description
        """
        messages.add_message(
            self.request, messages.ERROR,
            _("Please correct the error below."))
        return self.render_to_response(self.get_context_data(form=form))


class RoleUpdateView(DokumenUpdateView):
    """role Update View.

    Attributes:
        context_object_name (str): Description
        form_class (TYPE): Description
        model (TYPE): Description
        object (TYPE): Description
        pk_url_kwarg (str): Description
        template_name (str): Description
    """

    template_name = 'role/edit.html'
    model = Role
    form_class = forms.RoleForm
    pk_url_kwarg = 'id'

    def get_queryset(self):
        """Filter by type and customer.

        Returns:
            TYPE: Description
        """
        queryset = super(RoleUpdateView, self).get_queryset()
        return queryset

    def form_valid(self, form):
        """If the form is valid, save the associated model.

        Args:
            form (TYPE): Description

        Returns:
            TYPE: Description
        """
        self.object = form.save(commit=False)
        self.object.save()

        return super(RoleUpdateView, self).form_valid(form)

    def get_success_url(self):
        """get_success_url.

        Returns:
            TYPE: Description
        """
        messages.add_message(
            self.request, messages.SUCCESS,
            _("Successful update"))
        if 'save-and-add' in self.request.POST:
            return reverse('super:role-new')
        else:
            return reverse('super:role-edit', args=[self.object.id, ])

    def form_invalid(self, form):
        """form_invalid.

        Args:
            form (TYPE): Description

        Returns:
            TYPE: Description
        """
        messages.add_message(
            self.request, messages.ERROR,
            _("Please correct the error below."))
        return self.render_to_response(self.get_context_data(form=form))


class RoleDeleteView(DokumenDeleteView):
    """role Delete View.

    Attributes:
        model (TYPE): Description
        pk_url_kwarg (str): Description
        template_name (str): Description
    """

    template_name = 'role/delete.html'
    model = Role
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        """get_context_data.

        Args:
            **kwargs: Description

        Returns:
            TYPE: Description
        """
        context = super(
            RoleDeleteView, self).get_context_data(**kwargs)
        deletable_objects, model_count, protected = get_deleted_objects(
            [self.object])
        context['deletable_objects'] = deletable_objects
        context['model_count'] = dict(model_count).items()
        context['protected'] = protected
        #
        return context

    def get_queryset(self):
        """Filter by type and customer.

        Returns:
            TYPE: Description
        """
        queryset = super(RoleDeleteView, self).get_queryset()
        return queryset

    def get_success_url(self):
        """get_success_url.

        Returns:
            TYPE: Description
        """
        messages.add_message(
            self.request, messages.SUCCESS,
            _("Successful delete"))
        return reverse('super:roke-list')
