from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from .forms import TasksForm
from .serializers import TasksSerializer


class TasksFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            "title": "Test Task",
            "description": "Test description",
            "due_date": timezone.now().date()
        }

        form = TasksForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            "title": "",
            "description": "",
            "due_date": ""
        }

        form = TasksForm(data=form_data)
        self.assertFalse(form.is_valid(), form.errors)
        self.assertIn("title", form.errors)
        self.assertIn("description", form.errors)
        self.assertIn("due_date", form.errors)

    def test_past_time_date(self):
        form_data = {
            "title": "Test Task",
            "description": "Test description",
            "due_date": timezone.now().date() - timedelta(days=1),
        }
        form = TasksForm(data=form_data)
        self.assertFalse(form.is_valid(), form.errors)
        self.assertIn("due_date", form.errors)


class TasksSerializerTest(TestCase):
    def test_valid_serializer(self):
        data = {
            "title": "Test Task",
            "description": "Test description",
            "due_date": timezone.now().date(),
            "user": {
                "username": "admin",
                "email": "example@email.com"
            }
        }
        serializer = TasksSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_serializer(self):
        data = {
            "title": "",
            "description": "",
            "due_date": "",
            "user": {}
        }
        serializer = TasksSerializer(data=data)
        self.assertFalse(serializer.is_valid(), serializer.errors)
        self.assertIn("title", serializer.errors)
        self.assertIn("description", serializer.errors)
        self.assertIn("due_date", serializer.errors)

    def test_past_time_date(self):
        form_data = {
            "title": "Test Task",
            "description": "Test description",
            "due_date": timezone.now().date() - timedelta(days=1),
            "user": {
                "username": "test user",
                "email": "example@email.com"
            }
        }
        serializer = TasksSerializer(data=form_data)
        self.assertFalse(serializer.is_valid(), serializer.errors)
        self.assertIn("due_date", serializer.errors)
