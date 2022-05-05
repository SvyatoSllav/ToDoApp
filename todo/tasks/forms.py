from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Введите текст'})
    )

    class Meta:
        model = Task
        fields = ('title', )


class UpdateTaskForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Введите текст'})
    )
    description = forms.CharField(
        widget=forms.Textarea(),
    )

    class Meta:
        model = Task
        fields = ('title', 'description')
