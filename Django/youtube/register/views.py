from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from . import models
from django.contrib.auth import login,logout
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SnippetSerializer
# Create your views here.

def new_user(request):
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            login(request,form.save())
            return redirect("Dave:post")
    else:
        form=UserCreationForm()
    return render(request,'register/new_user.html',{"form":form})



def user_login(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("Dave:post")
    else:
        form=AuthenticationForm()
    return render(request,'register/user_login.html',{'form':form})


def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect("Dave:post")


@api_view(['GET'])
def getData(request):
    person={'name':'Dennis','age':28}
    return Response(person)