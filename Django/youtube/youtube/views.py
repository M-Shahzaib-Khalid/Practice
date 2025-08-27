from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import Group,User
from rest_framework import permissions, viewsets
from .serializers import GroupSerializer,UserSerializer

def Home(request):
    return render(request,"Home.html")
#    return HttpResponse("Welcome to Home Page!")

def About(request):
    return render(request,"about.html")
#    return HttpResponse("This is about page")


class USerViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset=Group.objects.all().order_by('name')
    serializer_class=GroupSerializer
    permission_classes=[permissions.IsAuthenticated]