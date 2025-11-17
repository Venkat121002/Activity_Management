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
    path('activitylog-detail/<int:id>/',views.activitylog_detail,name='activitylog_detail'),
    path('activitylog-edit/<int:id>/',views.activitylog_edit,name='activitylog_edit'),
    path('delete/<int:id>',views.activitylog_delete,name='activitylog_delete'),

    # form Remainder Model
    path('remainder-list',views.remainder_list,name='remainder_list'),
    path('create-remainder/',views.remainder_create,name='remainder_create'),
    path('remainder-edit/<int:id>/',views.remainder_edit,name='remainder_edit'),
    path('remainder-detail/<int:id>/',views.remainder_detail,name='remainder_detail'),
    path('remainder-delete/<int:id>',views.remainder_delete,name='remainder_delete'),
    
]
