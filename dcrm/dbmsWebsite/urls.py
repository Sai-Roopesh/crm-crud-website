
from . import views
from django.urls import path

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('home/',views.home,name='home'),
    path('welcome/',views.welcome,name='welcome'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),

]
