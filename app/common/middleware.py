"""."""
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class Middleware404(MiddlewareMixin):
    """."""

    def process_response(self, request, response):
        """."""
        if response.status_code == 404:
            return HttpResponseRedirect(reverse('super:home'))
        return response
