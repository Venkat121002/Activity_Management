from django import forms
from .models import Task, ActivityLog, Remainder

class TasksForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

class ActivityLogForm(forms.ModelForm):
    class Meta:
        model = ActivityLog
        fields = '__all__'

class RemainderForm(forms.ModelForm):
    class Meta:
        model = Remainder
        fields = '__all__'

