"""Mixins."""
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from app.common.models import Carpeta, Configuracion, Link
from app.accounts.models import Role
import datetime


class SuperPermissionsMixin(object):
    """SuperPermissionsMixin.

    Attributes:
        user_types (list): Description
    """

    user_types = []

    @classmethod
    def validate_permissions(cls, request):
        """Cl Validate permissions.

        Args:
            request (TYPE): Description

        Returns:
            TYPE: Description

        Raises:
            PermissionDenied: Description
        """
        if not request.user:
            raise PermissionDenied
        if not len(cls.user_types):
            if not request.user.is_super:
                raise PermissionDenied
        else:
            if request.user.user_type not in cls.user_types:
                raise PermissionDenied
        return True

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        """dispatch.

        Args:
            request (TYPE): Description
            *args: Description
            **kwargs: Description

        Returns:
            TYPE: Description
        """
        self.validate_permissions(request)

        return super(
            SuperPermissionsMixin,
            self
        ).dispatch(request, *args, **kwargs)


class FormsetMixin(object):
    """FormsetMixin.

    Attributes:
        object (TYPE): Description
    """

    object = None

    def get(self, request, *args, **kwargs):
        """get.

        Args:
            request (TYPE): Description
            *args: Description
            **kwargs: Description

        Returns:
            TYPE: Description
        """
        if getattr(self, 'is_update_view', False):
            self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset_class = self.get_formset_class()
        formset = self.get_formset(formset_class)
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset))

    def post(self, request, *args, **kwargs):
        """post.

        Args:
            request (TYPE): Description
            *args: Description
            **kwargs: Description

        Returns:
            TYPE: Description
        """
        if getattr(self, 'is_update_view', False):
            self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset_class = self.get_formset_class()
        formset = self.get_formset(formset_class)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def get_formset_class(self):
        """get_formset_class.

        Returns:
            TYPE: Description
        """
        return self.formset_class

    def get_formset(self, formset_class):
        """get_formset.

        Args:
            formset_class (TYPE): Description

        Returns:
            TYPE: Description
        """
        return formset_class(**self.get_formset_kwargs())

    def get_formset_kwargs(self):
        """get_formset_kwargs.

        Returns:
            TYPE: Description
        """
        kwargs = {
            'instance': self.object
        }
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    def form_valid(self, form, formset):
        """form_valid.

        Args:
            form (TYPE): Description
            formset (TYPE): Description

        Returns:
            TYPE: Description
        """
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return super(FormsetMixin, self).form_valid(form)

    def form_invalid(self, form, formset):
        """form_invalid.

        Args:
            form (TYPE): Description
            formset (TYPE): Description

        Returns:
            TYPE: Description
        """
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset))


class MenuMixin(object):
    """MenuMixin."""

    def get_context_data(self, **kwargs):   # noqa
        """get_context_data.

        Args:
            **kwargs: Description

        Returns:
            TYPE: Description
        """
        context = super(
            MenuMixin, self).get_context_data(**kwargs)
        try:
            folder_exclud = Role.objects.filter(
                id=self.request.user.role.id).values_list('folder', flat=True)
            parents = Carpeta.objects.exclude(id__in=folder_exclud).filter(
                padre=None).order_by('modified')
        except Exception:
            parents = Carpeta.objects.filter(
                padre=None).order_by('modified')
        link = Link.objects.all().order_by('name')
        try:
            settings = Configuracion.objects.get(id=1)
        except Exception:
            settings = False
        now = datetime.datetime.now()
        context.update({
            'carpetasMenu': parents,
            'settings': settings,
            'link_data': link,
            'time': now
        })
        return context


class SettingsMixin(object):
    """SettingsMixin."""

    def get_context_data(self, **kwargs):   # noqa
        """Summary

        Args:
            **kwargs: Description

        Returns:
            TYPE: Description
        """
        context = super(
            SettingsMixin, self).get_context_data(**kwargs)
        try:
            settings = Configuracion.objects.get(id=1)
        except Exception:
            settings = False
        now = datetime.datetime.now()

        context.update({
            'settings': settings,
            'time': now
        })
        return context
