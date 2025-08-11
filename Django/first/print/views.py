from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Database_model
# Create your views here.

def hello(request):
    allmembers=Database_model.objects.all().values()
    template=loader.get_template('models.html')
    context={
        'allmembers':allmembers,
    }
    return HttpResponse(template.render(context,request))

def details(request,id):
    allmembers=Database_model.objects.get(id=id)
    template=loader.get_template('details.html')
    context={
        'allmembers':allmembers
    }
    return HttpResponse(template.render(context,request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())