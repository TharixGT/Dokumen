"""Managers."""
# coding: utf-8
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """User Managers.

    Attributes:
        use_in_migrations (bool): Description
    """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and saves a User,username, email and password.

        Args:
            email (TYPE): Description
            password (TYPE): Description
            **extra_fields (TYPE): Description
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        """Create user.

        Args:
            email (None, optional): Description
            password (None, optional): Description
            **extra_fields (TYPE): Description
        """
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create superuser.

        Args:
            email (TYPE): Description
            password (TYPE): Description
            **extra_fields (TYPE): Description

        Raises:
            ValueError: Description
        """
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('user_type', 'admin')
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
