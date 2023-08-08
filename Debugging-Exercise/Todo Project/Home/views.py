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
        todos = Todo.objects.filter(request)
        context = {'todos': todos}
        return render(request, self.template_name, context)
    


class TodoDetailView(TodoMixin):
    template_name = 'Home/todo_detail.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


