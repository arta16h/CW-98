from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from .models import Todo
from .forms import TodoForm
from django.views import View


class TodoMixin:
    model = Todo
    form_class = TodoForm
    template_name = "Home/todo_detail.html"

    def dispatch(self, request, *args, **kwargs):
        todo = Todo.objects.get(id=kwargs['pk'])
        if not todo.user == request.user:
            raise PermissionDenied
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        todo = Todo.objects.get(kwargs['pk'])
        form = self.form_class()
        form = self.form_class()
        context = {'todo': todo, 'form':form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        todo = Todo.objects.get(kwargs['pk'])
        form = self.form_class(request.POST, instance=todo)
        if form.is_valid():
            todo.save()
            return redirect('thank_you')
        return render(request, self.template_name, {'todo': todo})
