from django.shortcuts import render,redirect,get_object_or_404
from .models import Task, ActivityLog, Remainder
from .forms import TasksForm, ActivityLogForm, RemainderForm
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'activity_app/home.html')

def task_list(request):
    tasks = Task.objects.order_by('-created_at')
    paginator = Paginator(tasks,5)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'total_tasks': tasks.count()
    }
    return render(request, 'activity_app/task_list.html',context)

def task_create(request):
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('task_list')
    else:
        form = TasksForm()

    return render(request, 'activity_app/task_form.html', {'form': form})

def edit_task(request,id):
    task = get_object_or_404(Task,id=id)
    if request.method == 'POST':
        form = TasksForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TasksForm(instance=task)
    return render(request,'activity_app/task_form.html',{'form':form})

def delete_task(request,id):
    task = get_object_or_404(Task,id=id)
    task.delete()
    return redirect('task_list')

def detail_task(request,id):
    task = get_object_or_404(Task,id=id)
    context = {
        'task': task
    }

    return render(request,'activity_app/task_detail.html',context)