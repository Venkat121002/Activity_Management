from django.shortcuts import render,redirect
from .models import Task, ActivityLog, Remainder
from .forms import TasksForm, ActivityLogForm, RemainderForm

# Create your views here.
def task_list(request):
    return render(request,'activity_app/base.html')