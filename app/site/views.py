"""Views."""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView, CreateView
from django.views.decorators.cache import never_cache
from django.shortcuts import render


class HomeView(TemplateView):
    """HomeView.

    Attributes:
        template_name (str): Description
    """

    template_name = 'home.html'

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
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
