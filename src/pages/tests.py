"""This module defines the tests for the pages of the HCI."""

# Third-party dependencies:
from django.test import TestCase


class ViewTests(TestCase):
    """Make sure the views of the HCI are behaving as expected."""

    def test_home_page(self):
        """The home page should return a status code of 200."""
        response = self.client.get("/", follow=True)
        self.assertEqual(response.status_code, 200)
