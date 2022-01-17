from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    return render(request,"writing/index.html")

def blog(request):
    
    postlist = Post.objects.all()
    return render(request,"writing/blog.html", { 'postlist' : postlist})

def posting(request,pk):
    post = Post.objects.get(pk=pk)
    return render(request, "writing/posting.html", {'post' : post})
