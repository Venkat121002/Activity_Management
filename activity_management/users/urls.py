from django.urls import path
from . import views
urlpatterns = [
    path('',views.login_view,name='login-page'),
    path('register/',views.registraion_view,name='register-page'),
    path('logout/',views.logout_view,name='logout-page'),
]
