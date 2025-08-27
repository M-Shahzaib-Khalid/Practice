from django.contrib import admin
from django.urls import path
from . import views

app_name='register'
urlpatterns=[
    path("new_user/",views.new_user,name='new'),
    path("login/",views.user_login,name='login'),
    path("logout/",views.logout_view,name='logout'),
    path("get/",views.getData),
]

