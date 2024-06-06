from django.test import TestCase, override_settings
from django.urls import reverse, resolve
from task_manager.statuses.views import (
    StatusIndexView,
    StatusCreateView,
    StatusUpdateView,
    StatusDeleteView
)


@override_settings(
    SECRET_KEY='fake-key',
)
class StatusUrlTest(TestCase):

    def test_status_index_url(self):
        url = reverse('statuses')
        self.assertEqual(resolve(url).func.view_class, StatusIndexView)

    def test_status_create_url(self):
        url = reverse('status_create')
        self.assertEqual(resolve(url).func.view_class, StatusCreateView)

    def test_status_update_url(self):
        url = reverse('status_update', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, StatusUpdateView)

    def test_status_delete_url(self):
        url = reverse('status_delete', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, StatusDeleteView)
