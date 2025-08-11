from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('print/',views.hello),
    path('print/details/<int:id>',views.details,name='details'),
]
