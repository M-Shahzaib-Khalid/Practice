from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from base import models
from base.models import Contact
# Create your views here.

def home(request):
    return render(request,'home.html')

def contact(request):
    if request.method=="POST":
        print("Post")
        name=request.POST.get('name')
        email=request.POST.get('email')
        content=request.POST.get('content')
        number=request.POST.get('number')
        print(name,email,content,number)

        if len(name)>1 and len(name)<40:
            pass
        else:
            messages.error(request,'length of name should be greater than 2 and less than 40')
            return render(request,'home.html')
        ins=models.Contact(name=name,email=email,content=content,number=number)
        ins.save()
        messages.success(request,'Thank You for contacting me')
        print('Data saved to database')
    return render(request,'home.html')