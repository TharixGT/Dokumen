from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from app.accounts.models import User


class SuperPermissionsMixin(object):
    user_types = []

    @classmethod
    def validate_permissions(self, request):
        if not request.user:
            raise PermissionDenied

        if not len(self.user_types):
            if not request.user.is_super:
                raise PermissionDenied
        else:
            if request.user.user_type not in self.user_types:
                raise PermissionDenied

        return True

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):

        self.validate_permissions(request)

        return super(
            SuperPermissionsMixin,
            self
        ).dispatch(request, *args, **kwargs)


class NotaryOrSuperPermissionsMixin(object):
    user_types = []

    @classmethod
    def validate_permissions(self, request):
        if not request.user:
            raise PermissionDenied

        if request.user.user_type == User.USER:
            raise PermissionDenied

        return True

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        self.validate_permissions(request)

        return super(
            NotaryOrSuperPermissionsMixin,
            self
        ).dispatch(request, *args, **kwargs)


class FormsetMixin(object):
    object = None

    def get(self, request, *args, **kwargs):
        if getattr(self, 'is_update_view', False):
            self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset_class = self.get_formset_class()
        formset = self.get_formset(formset_class)
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset))

    def post(self, request, *args, **kwargs):
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
        return self.formset_class

    def get_formset(self, formset_class):
        return formset_class(**self.get_formset_kwargs())

    def get_formset_kwargs(self):
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
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return super(FormsetMixin, self).form_valid(form)

    def form_invalid(self, form, formset):
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset))
