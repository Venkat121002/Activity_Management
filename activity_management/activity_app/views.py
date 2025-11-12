from django.shortcuts import render,redirect,get_object_or_404
from .models import Task, ActivityLog, Remainder
from .forms import TasksForm, ActivityLogForm, RemainderForm
from django.core.paginator import Paginator

# Create your views here.
def task_list(request):
    tasks = Task.objects.order_by('-created_at')
    paginator = Paginator(tasks,5)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'total_tasks': tasks.count()
    }
    return render(request, 'activity_app/base.html',context)

