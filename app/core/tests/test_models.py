from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_success(self):
        """Test creating a user with an email is successful"""
        test_email = 'fhgvk@jhba.com'
        test_password = 'password23'
        user = get_user_model().objects.create_user(
            email=test_email,
            password=test_password
        )

        self.assertEqual(user.email, test_email)
        self.assertTrue(user.check_password(test_password))

    def test_user_normalized_email(self):
        """tests that a user email is normalized"""

        email = "test@RDNBUDYY.COM"
        user = get_user_model().objects.create_user(
            email=email,
            password="test123"
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating new user w/o email raises error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_super_user(self):
        """test a valid super user can be created"""

        user = get_user_model().objects.create_superuser(
            "some@email.com",
            "somePwd"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
