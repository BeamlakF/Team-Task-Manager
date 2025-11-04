from django import forms
from .models import Task, Comment

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_completed', 'assigned_to', 'due_date']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

