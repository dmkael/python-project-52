from django.test import TestCase, override_settings
from django.urls import reverse, resolve
from task_manager.tasks.views import (
    TaskIndexView,
    TaskCreateView,
    TaskUpdateView,
    TaskDetailView,
    TaskDeleteView
)


@override_settings(
    SECRET_KEY='fake-key',
)
class TasksUrlTest(TestCase):

    def test_task_index_url(self):
        url = reverse('tasks')
        self.assertEqual(resolve(url).func.view_class, TaskIndexView)

    def test_task_create_url(self):
        url = reverse('task_create')
        self.assertEqual(resolve(url).func.view_class, TaskCreateView)

    def test_task_update_url(self):
        url = reverse('task_update', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, TaskUpdateView)

    def test_task_detail_url(self):
        url = reverse('task_detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, TaskDetailView)

    def test_task_delete_url(self):
        url = reverse('task_delete', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, TaskDeleteView)
