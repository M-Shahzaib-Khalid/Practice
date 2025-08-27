from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def post(request):
    p=Post.objects.all().order_by('-date')
    return render(request,'post/post_list.html',{'p':p })

def post_page(request,slug):
    ppost=Post.objects.get(slug=slug)
    return render(request,'post/post_page.html',{'ppost':ppost})

    
@login_required(login_url="/register/login/")
def post_new(request):
    if request.method=='POST':
        form=forms.CreatePost(request.POST,request.FILES)
        if form.is_valid():
            newpost=form.save(commit=False)
            newpost.author=request.user
            newpost.save()
            return redirect('Dave:post')
    else:
        form=forms.CreatePost()
    return render(request, 'post/post_new.html',{'form':form})