from django.test import TestCase
from task_manager.users.views import (
    UsersIndexView,
    UserCreateView,
    UserUpdateView,
    UserDeleteView
)
from django.urls import reverse, resolve


class UsersUrlTestCase(TestCase):

    def test_users_index_url(self):
        url = reverse('users')
        self.assertEqual(resolve(url).func.view_class, UsersIndexView)

    def test_users_create_url(self):
        url = reverse('user_create')
        self.assertEqual(resolve(url).func.view_class, UserCreateView)

    def test_user_update_url(self):
        url = reverse('user_update', kwargs={'id': 1})
        self.assertEqual(resolve(url).func.view_class, UserUpdateView)

    def test_user_delete_url(self):
        url = reverse('user_delete', kwargs={'id': 1})
        self.assertEqual(resolve(url).func.view_class, UserDeleteView)
