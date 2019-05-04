from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'test@eray.com'
        password = 'test'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'bla@TESTDOMAIN.COM'
        user = get_user_model().objects.create_user(email, 'some_password')

        self.assertEqual(user.email, email.lower())

    def test_user_invalid_email(self):
        """Valid emails."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_super_user(self):
        """Creating a new superuser."""
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'test'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
