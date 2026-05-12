from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone


class TasksForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    due_date = forms.DateField(
        initial=timezone.now(),
        widget=forms.DateInput(
            attrs={
                "class": "form-control",
                "type": "date",
                "min": timezone.now().date().isoformat()
            }
        )
    )

    def clean_due_date(self):
        due_date = self.cleaned_data['due_date']

        if due_date < timezone.now().date():
            raise ValidationError("Date cannot be in the past")

        return due_date