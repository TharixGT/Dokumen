"""Model."""
# coding: utf-8

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """User model.

    Attributes:
        ADMIN (str): Description
        CHOISE_USER_TYPE (TYPE): Description
        created (Datetime): Description
        email (String): Email is unique in all project
        first_name (String): First name of user
        is_active (Boolean): If user is active
        last_name (String): Last name of user
        modified (Datetime): Modified datetime
        objects (Queryset): Queryse Django
        REQUIRED_FIELDS (tuple): Description
        USER (str): Description
        user_type (TYPE): Choice (ADMIN, USER).
        USERNAME_FIELD (str): Description

    Deleted Attributes:
        address (String): Address of user
        company (String): Company of user
        dni (String): DNI is unique in all project
        is_admin (Boolean): True if user permission to admin
        phone_number (String): Phone number of user
        postal_code (String): Postal code of user
        province (ForeignKey): Province FK
        town (ForeignKey): Town FK
    """

    USER = 'user'
    ADMIN = 'admin'
    CHOISE_USER_TYPE = (
        (USER, _('User')),
        (ADMIN, _('Admin')),
    )

    REQUIRED_FIELDS = ('first_name', 'last_name')
    USERNAME_FIELD = 'email'

    user_type = models.CharField(
        max_length=5, blank=True, null=True,
        choices=CHOISE_USER_TYPE,
        verbose_name=_('User type')
    )

    email = models.EmailField(unique=True, verbose_name=_('Email'))
    first_name = models.CharField(max_length=50, verbose_name=_('First name'))
    last_name = models.CharField(max_length=50, verbose_name=_('Last name'))
    is_active = models.BooleanField(default=False, verbose_name=_('Is active'))

    created = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name=_('Created'))
    modified = models.DateTimeField(
        auto_now=True, editable=False, verbose_name=_('Modified'))

    objects = UserManager()

    class Meta:
        """class.

        Attributes:
            db_table (str): Description
            verbose_name (TYPE): Description
            verbose_name_plural (TYPE): Description
        """

        verbose_name = _('User')
        verbose_name_plural = _('Users')
        db_table = 'auth_user'

    @property
    def username(self):
        """Return username."""
        return self.email

    @property
    def get_short_name(self):
        """Return short name."""
        return self.email

    @property
    def is_staff(self):
        """Return staff."""
        return self.is_admin

    @property
    def full_name(self):
        """Return full name."""
        return self.get_full_name()

    @property
    def is_user(self):
        """Return user."""
        return self.user_type == self.USER

    @property
    def is_admin(self):
        """Return admin."""
        return self.user_type == self.ADMIN

    @property
    def is_super(self):
        """Return super."""
        return self.user_type == self.ADMIN

    def get_full_name(self):
        """Full name of user.

        Returns:
            String: u'%s %s' % (self.first_name, self.last_name)
        """
        return u'%s %s' % (self.first_name, self.last_name)
