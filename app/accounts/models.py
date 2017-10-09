"""Model."""
# coding: utf-8

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from managers import UserManager
import uuid


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
    MANAGER = 'manager'
    CHOISE_USER_TYPE = (
        (USER, _('User')),
        (ADMIN, _('Admin')),
        (MANAGER, _('Manager')),
    )

    REQUIRED_FIELDS = ('first_name', 'last_name')
    USERNAME_FIELD = 'email'

    user_type = models.CharField(
        max_length=7, blank=False, null=False,
        choices=CHOISE_USER_TYPE,
        verbose_name=_('Type')
    )

    email = models.EmailField(unique=True, verbose_name=_('Email'))
    first_name = models.CharField(max_length=50, verbose_name=_('First name'))
    last_name = models.CharField(max_length=50, verbose_name=_('Last name'))
    is_active = models.BooleanField(default=False, verbose_name=_('Is active'))
    role = models.ForeignKey(
        'Role', null=True, blank=True, verbose_name=_('Role'))
    created = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name=_('Created'))
    modified = models.DateTimeField(
        auto_now=True, editable=False, verbose_name=_('Modified'))
    force_change_password = models.BooleanField(default=True)
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

    @property
    def is_manager(self):
        """Return manager."""
        return self.user_type == self.MANAGER

    def get_full_name(self):
        """Full name of user.

        Returns:
            String: u'%s %s' % (self.first_name, self.last_name)
        """
        return u'%s %s' % (self.first_name, self.last_name)

    @staticmethod
    def get_or_register(email, first_name, last_name, user_type):
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
                first_name=first_name,
                last_name=last_name,
                user_type=user_type,
                is_active=True)
            user.set_password(password)
            user.save()
        else:
            user = User.objects.get(email=email)
            user.save()
            password = None
        return user, password


class Role(models.Model):
    """Archivo.

    Attributes:
        carpetas (TYPE): Description
        id (TYPE): Description
        nombre (TYPE): Description
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=75, null=False,
        blank=False, verbose_name=_('Name'))
    folder = models.ManyToManyField(
        'common.carpeta', verbose_name=_('Folder'),
        help_text=_('select the folders you want to exclude'))
    created = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name=_('Created'))
    modified = models.DateTimeField(
        auto_now=True, editable=False, verbose_name=_('Modify'))

    class Meta:
        """Meta.

        Attributes:
            db_table (str): Description
            default_related_name (str): Description
            verbose_name (TYPE): Description
            verbose_name_plural (TYPE): Description

        """

        verbose_name = _('Role')
        verbose_name_plural = _('Roles')
        default_related_name = 'role'
        db_table = 'role'

    def __unicode__(self):
        """Unicode.

        Returns:
            TYPE: Description
        """
        return str(self.name)
