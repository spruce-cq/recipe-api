from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        """Test creating a new user successful"""

        email = "test@test.com"
        password = "testpassword1"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(raw_password=password))

    def test_new_user_email_normalized(self):
        """Test the email of a new user is normalized"""

        email = "test@TEST.com"
        user = get_user_model().objects.create_user(email=email, password="testpassword")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with invalid email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "testpassword")


    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            "testsuper@super.com",
            "super123",
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
