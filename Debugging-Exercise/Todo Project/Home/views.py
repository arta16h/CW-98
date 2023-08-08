from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo, Post
from .mixins import TodoMixin


class IndexView(View):
    template_name = 'Home/todo_list.html'
    def get(self, request):
        return render(request, self.template_name)


class TodoListView(View):
    template_name = 'Home/todo_list.html'
    def get(self, request) :
        if request.user.is_authenticated:
            todos = Todo.objects.filter(user=request.user)
            return render(request, self.template_name, {'todos': todos})
        else:
            return render(request, self.template_name)
    

class TodoDetailView(View):
    template_name = 'Home/todo_detail.html'
    def get(self, request):
        return render(request, self.template_name)
    
class Thanks(View):
    template_name = "Home/thankyou.html"

    def get(self, request):
        return render(request, self.template_name)


def update_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        content = request.POST.get("content")
        Post.content = content
        Post.save()
        return redirect("post_details", id=id)
    else:
        return render(request, "post.html", {"post": post})

