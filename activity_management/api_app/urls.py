from api_app.views import TaskApiView,ActivitylogApiView,RemainderApiView
from django.urls import path
urlpatterns = [
    path('task-api/',TaskApiView.as_view(),name='taskapiview'),
    path('activity-api/',ActivitylogApiView.as_view(),name='activitylogview'),
    path('remainder-api/',RemainderApiView.as_view(),name='remainderview'),
]
