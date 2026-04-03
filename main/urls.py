from django.urls import path

from . import views 
urlpatterns = [
    path('register/',views.registration , name='register'),
    path('login/' , views.logins, name='login'),
    path('',views.home , name='home'),
    path('superhome/',views.superhome , name='superhome'),
    path('logout/',views.logout_view , name='logout'),
    path('superphone/<int:id>/',views.superphone , name='superphone'),
    path('superlaptop/<int:id>/',views.superlaptop,name='superlaptop'),
    path('phonesdetail/<int:id>/',views.phonesdetail ,name='phonesdetail'),
    path('laptopdetail/<int:id>/',views.laptopdetail , name='laptopdetail'),
    
]