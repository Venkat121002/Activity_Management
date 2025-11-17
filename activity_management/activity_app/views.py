from django.shortcuts import render,redirect,get_object_or_404
from .models import Task, ActivityLog, Remainder
from .forms import TasksForm, ActivityLogForm, RemainderForm
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'activity_app/home.html')

def task_list(request):
    search_querey = request.GET.get('search','')
    
    tasks = Task.objects.order_by('-created_at')

    if search_querey:
        tasks = tasks.filter(title__icontains=search_querey)

    paginator = Paginator(tasks,5)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_querey,
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
        print(form)
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

def activitylog_list(request):
    activities = ActivityLog.objects.order_by('-performed_at')
    paginator = Paginator(activities,5)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'total_activities': activities.count()
    }

    return render(request,'activity_app/activitylog_list.html',context)

def activitylog_create(request):
    if request.method == 'POST':
        form = ActivityLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('activitylog_list')
    else:
        form = ActivityLogForm()
    return render(request,'activity_app/activitylog_form.html',{'form':form})

def activitylog_detail(request,id):
    activity = get_object_or_404(ActivityLog,id=id)
    context = {
        'activity': activity
    }

    return render(request,'activity_app/activitylog_detail.html',context)

def activitylog_edit(request,id):
    activity = get_object_or_404(ActivityLog,id=id)
    if request.method == 'POST':
        form = ActivityLogForm(request.POST,instance=activity)
        if form.is_valid():
            form.save()
            return redirect('activitylog_list')
    else:
        form = ActivityLogForm(instance=activity)

    return render(request,'activity_app/activitylog_form.html',{'form':form})

def activitylog_delete(request,id):
    activity = get_object_or_404(ActivityLog,id=id)
    activity.delete()
    return redirect('activitylog_list')


def remainder_list(request):
    remainder = Remainder.objects.order_by('-created_at')
    pagination = Paginator(remainder,5)
    page_number = request.GET.get('page',1)
    page_obj = pagination.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'total_remainders': remainder.count()
    }

    return render(request,'activity_app/remainder_list.html',context)

def remainder_create(request):
    if request.method == 'POST':
        form = RemainderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('remainder_list')
    else:
        form = RemainderForm()
    return render(request,'activity_app/remainder_form.html',{'form':form})

def remainder_edit(request,id):
    remainder = get_object_or_404(Remainder,id=id)
    if request.method == 'POST':
        form = RemainderForm(request.POST,instance=remainder)
        if form.is_valid():
            form.save()
            return redirect('remainder_list')
    else:
        form = RemainderForm(instance=remainder)
    return render(request,'activity_app/remainder_form.html',{'form':form})

def remainder_detail(request,id):
    remainder = get_object_or_404(Remainder,id=id)
    context = {
        'remainder':remainder
    }

    return render(request,'activity_app/remainder_detail.html',context)

def remainder_delete(request,id):
    remainder = get_object_or_404(Remainder,id=id)
    remainder.delete()
    return redirect('remainder_list')