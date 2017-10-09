# -*- coding: utf-8 -*-
"""Coupons CRUD."""

from app.super.generics import DokumenListView, DokumenFormView, \
    DokumenUpdateView, DokumenDeleteView, DokumenUpdatePasswordView
from . import forms
from mail_templated import send_mail
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from app.common.utils import get_deleted_objects
from django.views.decorators.cache import never_cache
from django.db.models import Q
from django.conf import settings
from app.common.models import Configuracion
from django.contrib.auth import get_user_model
from app.super.mixins import SuperPermissionsMixin
from django.contrib.sites.models import Site
User = get_user_model()


class UserListView(SuperPermissionsMixin, DokumenListView):
    """User List View."""

    template_name = 'accounts/list.html'
    model = User
    context_object_name = 'users'
    paginate_by = 10
    ordering = ['email', 'first_name']

    def get_queryset(self):
        """Filter by type and customer."""
        queryset = super(UserListView, self).get_queryset()
        queryset = queryset.filter()
        return queryset


class UserNewView(DokumenFormView):
    """."""

    template_name = 'accounts/create.html'
    form_class = forms.NewUserForm
    success_url = reverse_lazy('super:user-list')
    model = User

    def get_context_data(self, **kwargs):   # noqa
        context = super(UserNewView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        # self.object = form.save(commit=False)
        self.object = form.save(commit=False)
        email = form.cleaned_data['email']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        user_type = form.cleaned_data['user_type']
        settingssite = Configuracion.objects.get(id=1)
        current_site = Site.objects.get_current()

        user, password = User.get_or_register(
            email, first_name, last_name, user_type)
        if user:
            send_mail(
                'email/email_data_register.html',
                {
                    'user': user,
                    'password': password,
                    'settingssite': settingssite,
                    'current_site': current_site.domain,
                },
                settings.DEFAULT_FROM_EMAIL,
                [user],
            )
            return super(UserNewView, self).form_valid(form)

        else:
            return self.form_invalid(form)

    def get_success_url(self):
        """."""
        messages.add_message(
            self.request, messages.SUCCESS,
            _("Successful creation"))
        if 'save-and-add' in self.request.POST:
            return reverse('super:user-new')
        else:
            return reverse('super:user-list')

    def form_invalid(self, form):
        """."""
        messages.add_message(
            self.request, messages.ERROR,
            _("Please correct the error below."))
        return self.render_to_response(self.get_context_data(form=form))


class UserUpdateView(DokumenUpdateView):
    """User Update."""

    template_name = 'accounts/edit.html'
    model = User
    form_class = forms.UserForm
    pk_url_kwarg = 'id'
    context_object_name = 'user'

    def get_queryset(self):
        """Filter by type and customer."""
        queryset = super(UserUpdateView, self).get_queryset()
        return queryset

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        # self.object.set_password(self.request.POST['password'])
        self.object.save()

        return super(UserUpdateView, self).form_valid(form)

    def get_success_url(self):
        """."""
        messages.add_message(
            self.request, messages.SUCCESS,
            _("Successful update"))
        if 'save-and-add' in self.request.POST:
            return reverse('super:user-new')
        else:
            return reverse('super:user-edit', args=[self.object.id, ])

    def form_invalid(self, form):
        """."""
        messages.add_message(
            self.request, messages.ERROR,
            _("Please correct the error below."))
        return self.render_to_response(self.get_context_data(form=form))


class UserDeleteView(DokumenDeleteView):
    """User Delete."""

    template_name = 'accounts/delete.html'
    model = User
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        """Judge Delete."""
        context = super(UserDeleteView, self).get_context_data(**kwargs)  # noqa
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
        queryset = super(UserDeleteView, self).get_queryset()
        return queryset

    def get_success_url(self):
        """."""
        messages.add_message(
            self.request, messages.SUCCESS,
            _("Successful delete"))
        return reverse('super:user-list')


class SearchView(DokumenListView):
    """SearchView.

    Attributes:
        context_object_name (str): Description
        queryset (TYPE): Description
        template_name (str): Description
    """

    template_name = 'accounts/list.html'
    queryset = User.objects.all()
    context_object_name = 'users'

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
            queryset = queryset.filter(
                Q(first_name__icontains=search_text) |
                Q(last_name__icontains=search_text) |
                Q(email__icontains=search_text)

            )
        return queryset.order_by('first_name')

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


class ChangePasswordView(DokumenUpdatePasswordView):
    """User Update."""

    template_name = 'accounts/password_change.html'
    model = User
    form_class = forms.CustomChangePasswordForm1
    pk_url_kwarg = 'id'
    context_object_name = 'user'

    def get_queryset(self):
        """Filter by type and customer."""
        queryset = super(ChangePasswordView, self).get_queryset()
        return queryset

    def get_context_data(self, **kwargs):   # noqa
        context = super(ChangePasswordView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        p1 = self.request.POST['password']
        p2 = self.request.POST['repeat_password']

        if p1 != p2:
            msg = _("Las contraseñas no coinciden.")
            form.add_error('password', msg)
            messages.add_message(
                self.request, messages.ERROR, "Las contraseñas no coinciden.")
            return self.render_to_response(self.get_context_data(form=form))

        self.object.set_password(p1)
        self.object.save()

        return super(ChangePasswordView, self).form_valid(form)

    def get_success_url(self):
        """."""
        messages.add_message(
            self.request, messages.SUCCESS,
            _("Successful password update"))

        return reverse('super:user-list')

    def form_invalid(self, form):
        """."""
        messages.add_message(
            self.request, messages.ERROR,
            _("Please correct the error below."))
        return self.render_to_response(self.get_context_data(form=form))
