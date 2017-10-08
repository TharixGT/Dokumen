"""Viws."""
from app.accounts.models import User
from . import generics


class HomeView(generics.KualitteTemplateView):
    """HomeView.

    Attributes:
        template_name (str): Description
        user_types (TYPE): Description
    """

    user_types = [User.ADMIN, User.USER]
    template_name = 'super/home.html'
