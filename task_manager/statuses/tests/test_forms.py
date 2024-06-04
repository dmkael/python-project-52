from django.test import TestCase, override_settings
from task_manager.statuses.forms import StatusForm
import os
import yaml


@override_settings(
    SECRET_KEY='fake-key'
)
class TestUserCreationForm(TestCase):

    def setUp(self):
        with open(
                os.path.join(
                    os.path.dirname(__file__),
                    'fixtures', 'forms.yaml'
                ),
                'r') as file:
            self.form_data = yaml.safe_load(file)

    def test_creation_form_with_valid_data(self):
        form = StatusForm(self.form_data.get('status1'))
        self.assertTrue(form.is_valid())

    def test_creation_form_with_invalid_data(self):
        form = StatusForm(self.form_data.get('status2'))
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors['name'])
        self.assertEqual(len(form.errors), 1)

    def test_creation_form_with_no_data(self):
        form = StatusForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
