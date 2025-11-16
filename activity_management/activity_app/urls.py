from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    # for task model
    path('task-list/',views.task_list,name='task_list'),
    path('create-task/',views.task_create,name='task_create'),
    path('edit-task/<int:id>/',views.edit_task,name='task_edit'),
    path('delete/<int:id>/',views.delete_task,name='task_delete'),
    path('detail/<int:id>',views.detail_task,name='task_detail'),

    # for activity model
    path('activitylog-list/',views.activitylog_list,name='activitylog_list'),
    path('create-activity/',views.activitylog_create,name='activitylog_create'),

]
