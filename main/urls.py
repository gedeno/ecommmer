from django.urls import path

from . import views 
urlpatterns = [
    path('register/',views.registration , name='register'),
    path('login/' , views.logins, name='login'),
    path('',views.home , name='home'),
]