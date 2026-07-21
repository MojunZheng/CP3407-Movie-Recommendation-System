from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import Mock, patch

from .models import User


class Practical8MockObjectTests(TestCase):
    """Mock object test for Practical 8."""

    def setUp(self):
        self.client = Client()
        self.real_user = User.objects.create(
            name="mock_login_user",
            password="mock_password",
            email="mock_login_user@example.com",
        )

    def test_mock_user_login_process_sets_session(self):
        """
        This test uses a mock object to simulate a successful user login process.
        The real user database query in the login view is replaced with a mock query result.
        """
        mock_user = Mock()
        mock_user.id = self.real_user.id

        with patch("movie.views.User.objects.filter") as mock_filter:
            mock_query_result = Mock()
            mock_query_result.first.return_value = mock_user
            mock_filter.return_value = mock_query_result

            response = self.client.post(
                reverse("movie:login"),
                {
                    "name": "mock_login_user",
                    "password": "mock_password",
                    "remember": 1,
                },
            )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session.get("user_id"), self.real_user.id)
        mock_filter.assert_called_once_with(
            name="mock_login_user",
            password="mock_password",
        )