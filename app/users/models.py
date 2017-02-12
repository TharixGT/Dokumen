"""Models of User.

Models of users
"""

from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from django.db import models
from .managers import UserManager
import uuid
import pytz


class User(AbstractBaseUser, PermissionsMixin):
    """User Model.

    Attributes:
        created (date): Creation date
        email (str): Email of user
        first_name (str): First name of user
        identifier (str): Identifier of user (Email)
        is_active (bool): If user is active = True
        is_admin (bool): If user is admin = True
        last_name (str): Last name of user
        modified (date): Date
    """

    USERNAME_FIELD = 'identifier'
    REQUIRED_FIELDS = ['email']

    identifier = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    force_change_password = models.BooleanField(default=True)
    timezone = models.CharField(
        _('Time Zone'),
        max_length=50, null=True, blank=True,
        choices=[(t, t) for t in pytz.common_timezones],
        default='Europe/Madrid')

    objects = UserManager()

    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        """Meta class of User model.

        Attributes:
            db_table (str): Table name
        """

        db_table = 'auth_user'

    def __str__(self):
        """Str representation of row.

        Returns:
            str: Identifier of User
        """
        return self.identifier

    def get_full_name(self):
        """Get full name of user.

        Returns:
            str: First name + Last name
        """
        return '{} {}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        """Get short name.

        Returns:
            str: Email of user
        """
        return self.email

    @property
    def is_staff(self):
        """If user is staff.

        Returns:
            bool: Return True if user is admin
        """
        return self.is_admin

    @property
    def full_name(self):
        """Get full name of user.

        Returns:
            str: super to get_full_name()
        """
        return self.get_full_name()

    @property
    def is_participant(self):
        """If user is participant return True.

        Returns:
            bool: Return True if user is a participant
        """
        if hasattr(self, 'participants'):
            if self.participants.count() > 0:
                return True
        return False

    @property
    def is_customer(self):
        """If user is customer return True.

        Returns:
            bool: Return True if user is a customer
        """
        return self.customer.all().count() > 0

    @property
    def is_judge(self):
        """If user is judge return True.

        Returns:
            bool: Return True if user is a judge
        """
        if hasattr(self, 'judge'):
            if self.judge.count() > 0:
                return True
        return False

    def reset_password(self):
        """Reset password.

        Returns:
            String: New random password
        """
        password = uuid.uuid4().hex[:6].upper()
        self.set_password(password)
        self.force_change_password = True
        self.save()
        return password

    @staticmethod
    def get_or_register(email, first_name, last_name, timezone):
        """Get or Register user.

        Args:
            email (str): Email of user
            first_name (str): First name
            last_name (str): Last name

        Returns:
            User: user
        """
        password = uuid.uuid4().hex[:6].upper()
        user = None
        if not User.objects.filter(email=email).exists():
            user = User.objects.create(
                email=email,
                identifier=email,
                first_name=first_name,
                last_name=last_name,
                timezone=timezone,
                is_active=True)
            user.set_password(password)
            user.save()
        else:
            user = User.objects.get(email=email)
            user.save()
            password = None
        return user, password
