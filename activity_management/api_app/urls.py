from api_app.views import TaskApiView,ActivitylogApiView,RemainderApiView
from django.urls import path
urlpatterns = [
    path('task-api/',TaskApiView.as_view(),name='taskapiview'),
    path('task-api/<int:id>',TaskApiView.as_view(),name='taskapi-edit'),
    path('task-api/<int:id>',TaskApiView.as_view(),name='taskapi-delete'),
    path('activity-api/',ActivitylogApiView.as_view(),name='activitylogview'),
    path('activity-api/<int:id>',ActivitylogApiView.as_view(),name='activityapi-edit'),
    path('activity-api/<int:id>',ActivitylogApiView.as_view(),name='activityapi-delete'),
    path('remainder-api/',RemainderApiView.as_view(),name='remainderview'),
    path('remainder-api/<int:id>',RemainderApiView.as_view(),name='remainder-edit'),
    path('remainder-api/<int:id>',RemainderApiView.as_view(),name='remainder-delete'),
]
