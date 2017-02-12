# -*- coding: utf-8 -*-
"""Tests of Users Blindjupp.

Attributes:
    User (TYPE): Description
"""

from django.test import TestCase

from django.contrib.auth import get_user_model

from mixer.backend.django import mixer
from blindjupp.customers import models as customer_models
from blindjupp.judges import models as judges_models
# from blindjupp.participants import models as participants_models

User = get_user_model()


class UserModelTestCase(TestCase):
    """Test Model User."""

    def setUp(self):
        """Setup test case."""
        self.user = mixer.blend(User)

    def test_user_is_customer(self):
        """Verify if user is a customer."""
        self.customer = mixer.blend(customer_models.Customer, user=self.user)
        self.assertEqual(self.user.is_customer, True)

    def test_user_is_judge_in_customer(self):
        """Verify if user is a customer."""
        self.customer = mixer.blend(customer_models.Customer)
        self.judge = mixer.blend(
            judges_models.Judge,
            user=self.user,
            customer=self.customer)
        user_is_judge = self.customer.user_is_judge(
            self.user.id)
        self.assertEqual(user_is_judge, True)
