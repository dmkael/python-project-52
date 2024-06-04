from django.test import TestCase, override_settings
from django.urls import reverse, resolve
from task_manager.statuses.views import (
    StatusIndexView,
    StatusCreateView,
    StatusUpdateView,
    StatusDeleteView
)
import os


@override_settings(
    SECRET_KEY='fake-key',
    FIXTURE_DIRS=[os.path.join(os.path.dirname(__file__), 'fixtures')]
)
class UsersUrlTestCase(TestCase):
    fixtures = ['users.yaml', 'statuses.yaml']

    def test_statuses_index_url(self):
        url = reverse('statuses')
        self.assertEqual(resolve(url).func.view_class, StatusIndexView)

    def test_statuses_create_url(self):
        url = reverse('status_create')
        self.assertEqual(resolve(url).func.view_class, StatusCreateView)

    def test_status_update_url(self):
        url = reverse('status_update', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, StatusUpdateView)

    def test_status_delete_url(self):
        url = reverse('status_delete', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, StatusDeleteView)
