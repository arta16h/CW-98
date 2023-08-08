from django.shortcuts import render
from django.views import View
from .models import Todo
from .mixins import TodoMixin


class IndexView(View):
    template_name = 'Home/todo_list.html'
    def get(self, request):
        return render(request, self.template_name)


class TodoListView(View):
    template_name = 'Home/todo_list.html'
    def get(self, request, *args, **kwargs):
        todos = Todo.objects.all()
        return render(request, self.template_name, {'todos': todos})
    


class TodoDetailView(TodoMixin, View):
    template_name = 'Home/todo_detail.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


