from django.urls import path
from . import views

urlpatterns = [
    path('',views.task_list,name='task_list'),
    path('create task/',views.task_create,name='task_create'),
    path('edit task/<int:id>/',views.edit_task,name='task_edit'),
    path('delete/<int:id>/',views.delete_task,name='task_delete'),
]
