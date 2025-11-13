from django.shortcuts import render,redirect,get_object_or_404
from .models import Task, ActivityLog, Remainder
from .forms import TasksForm, ActivityLogForm, RemainderForm
from django.core.paginator import Paginator
from django.contrib import messages

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

def task_create(request):
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            task = form.save()
            messages.success(request, f'Task "{task.title}" created successfully!')
            return redirect('task_list')
        else:
            messages.error(request, "Please correct the error")
    else:
        form = TasksForm()

    return render(request, 'activity_app/task_form.html', {'form': form})
