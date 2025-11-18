from django import forms
from .models import Task, ActivityLog, Remainder

class TasksForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type':'date'}),
            'due_date': forms.DateInput(attrs={'type':'date'}),
            'completed_date': forms.DateInput(attrs={'type':'date'}),
        }

class ActivityLogForm(forms.ModelForm):
    class Meta:
        model = ActivityLog
        fields = '__all__'

class RemainderForm(forms.ModelForm):
    class Meta:
        model = Remainder
        fields = '__all__'
        widgets = {
            'remainder_date': forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'sent_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

