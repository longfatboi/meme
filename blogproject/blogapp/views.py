from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def getpost(request, postId):
    post = Post.objects.get(id = postId)
    posts = Post.objects.all()
    return render(request, 'post.html', {'post':post, 'posts':posts})

