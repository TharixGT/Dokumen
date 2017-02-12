from __future__ import unicode_literals

from django.contrib.auth.models import (
    BaseUserManager,
)


class UserManager(BaseUserManager):

    def create_user(self, identifier, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not identifier:
            raise ValueError('Users must have an identifier')
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            identifier=identifier,
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, identifier, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            identifier=identifier, email=email, password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user
