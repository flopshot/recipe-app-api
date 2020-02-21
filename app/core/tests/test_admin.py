from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin_user@email.com",
            password="somePwd"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="some@guy.com",
            password="pwd123",
            name="Test User Name"
        )

    def test_users_listed(self):
        """test that users are listed on user page"""

        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.user.email)
        self.assertContains(res, self.user.name)

    def test_change_page(self):
        """test that editing page of user in admin works"""

        url = reverse("admin:core_user_change", args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        """test that the create user page works"""

        url = reverse("admin:core_user_add")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
