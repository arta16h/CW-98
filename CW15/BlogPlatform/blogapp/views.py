from django.shortcuts import render
from .models import Post

def home(request):
    return render(request,'home.html')

def all_post(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "post.html", context)