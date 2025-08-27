# from django.contrib import admin
from django.urls import path
from . import views

app_name='Dave'
urlpatterns = [
    path("",views.post,name='post'),
    path("new-post/",views.post_new,name='new_post'),
    path("<slug:slug>",views.post_page,name='page'),
]
