# todo/todo_app/forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title"]  # タスクのタイトルのみ入力可能
