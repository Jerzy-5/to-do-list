from django import forms
from .models import Task, Tag

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

        widgets = {
            "datetime": forms.DateTimeInput(
                attrs={"type": "datetime-local"}
            ),
            "deadline": forms.DateTimeInput(
                attrs={"type": "datetime-local"}
            ),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"