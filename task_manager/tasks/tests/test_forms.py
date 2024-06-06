from django.test import TestCase, override_settings
from task_manager.tasks.forms import TaskForm
import os
import yaml


@override_settings(
    SECRET_KEY='fake-key',
    FIXTURE_DIRS=[os.path.join(os.path.dirname(__file__), 'fixtures')]
)
class TaskCreationFormTest(TestCase):
    fixtures = ['users', 'statuses']

    def setUp(self):
        with open(
                os.path.join(
                    os.path.dirname(__file__),
                    'fixtures', 'forms.yaml'
                ),
                'r') as file:
            self.form_data = yaml.safe_load(file)

    def test_creation_form_with_valid_data(self):
        form = TaskForm(self.form_data.get('Task1'))
        self.assertTrue(form.is_valid())

    def test_creation_form_with_invalid_data(self):
        form = TaskForm(self.form_data.get('Task2'))
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors['name'])
        self.assertTrue(form.errors['status'])
        self.assertEqual(len(form.errors), 2)

    def test_creation_form_with_no_data(self):
        form = TaskForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)
