"""Test.

Attributes:
    User (TYPE): Description
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
# from django.core.urlresolvers import reverse

User = get_user_model()


class SignUpViewTestCase(TestCase):
    """Sign Up View Test Case."""

    def test_load_ok(self):
        """Test load ok."""
        # resp = self.client.get(reverse('account_signup'))
        # self.assertEqual(resp.status_code, 200)


class LoginViewTestCase(TestCase):
    """Login View Test Case."""

    def test_load_ok(self):
        """Test load ok."""
        # resp = self.client.get(reverse('account_login'))
        # self.assertEqual(resp.status_code, 200)
