"""Define tests for the HCI."""

from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from hci.forms import CustomSignUpForm


class ViewTests(TestCase):
    """Make sure the views of the HCI are behaving as expected."""

    def test_home_page(self) -> None:
        """The home page should return a status code of 200."""
        response = self.client.get("/", follow=True)
        self.assertEqual(response.status_code, 200)


class SignupViewTests(TestCase):
    """Make sure the signup view works as expected."""

    def setUp(self) -> None:
        """Set up the test environment."""
        self.client = Client()
        self.signup_url = reverse("signup")
        self.user_data = {
            "username": "test_user",
            "email": "test@example.com",
            "first_name": "Test",
            "last_name": "User",
            "password1": "secure_password_123",
            "password2": "secure_password_123",
        }

    def test_signup_page_loads(self) -> None:
        """Make sure the signup page loads correctly with a GET request."""
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")
        self.assertIsInstance(response.context["form"], CustomSignUpForm)

    def test_signup_successful(self) -> None:
        """Make sure a user can successfully sign up with valid data."""
        response = self.client.post(self.signup_url, self.user_data)

        # Check we're redirected to home page.
        self.assertRedirects(response, reverse("home"))

        # Check user was created in the database.
        self.assertTrue(User.objects.filter(username="test_user").exists())

        # Check user is logged in.
        user = response.wsgi_request.user
        self.assertTrue(user.is_authenticated)
        if isinstance(user, User):
            self.assertEqual(user.username, "test_user")
            self.assertEqual(user.email, "test@example.com")
            self.assertEqual(user.first_name, "Test")
            self.assertEqual(user.last_name, "User")

    def test_signup_invalid_form(self) -> None:
        """Make sure we can't sign up with invalid data."""

        # Remove required field.
        invalid_data = self.user_data.copy()
        invalid_data.pop("email")

        response = self.client.post(self.signup_url, invalid_data)

        # The form should be returned with validation errors.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")
        self.assertFalse(response.context["form"].is_valid())

        # Check user wasn't created.
        self.assertFalse(User.objects.filter(username="test_user").exists())

    def test_signup_password_mismatch(self) -> None:
        """Make sure we can't sign up when passwords don't match."""
        invalid_data = self.user_data.copy()
        invalid_data["password2"] = "different_password"

        response = self.client.post(self.signup_url, invalid_data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")
        self.assertFalse(response.context["form"].is_valid())
        self.assertIn("password2", response.context["form"].errors)

        # Check user wasn't created.
        self.assertFalse(User.objects.filter(username="test_user").exists())

    def test_signup_duplicate_username(self) -> None:
        """Make sure we can't sign up with a duplicate username."""

        # Create a user first.
        User.objects.create_user(
            username="test_user", email="existing@example.com", password="password_123"
        )

        response = self.client.post(self.signup_url, self.user_data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")
        self.assertFalse(response.context["form"].is_valid())
        self.assertIn("username", response.context["form"].errors)

        # Only the original user should exist.
        self.assertEqual(User.objects.filter(username="test_user").count(), 1)
