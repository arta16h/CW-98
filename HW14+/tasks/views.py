from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView
from django.views import View
from django.core.paginator import Paginator
from django.shortcuts import redirect
from .models import Task, Category, Tag, Create_Category,Create_Task
from .forms import TaskUpdateForm



def home(request):
    tasks = Task.objects.all()
    # paginator = Paginator(tasks, 4)
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)
    return render(request, "home.html", {"page_obj": tasks})


def search(request):
    query = request.GET.get("query", None)
    if query is not None:
        tasks = Task.objects.filter(title__icontains=query) | Task.objects.filter(
            tags__name__icontains=query
        )
        return render(request, "search.html", {"tasks": tasks})
    else:
        return render(request, "search.html", {})


def task_page(request):
    tasks_todo = Task.objects.filter(status="to-do")
    tasks_in_progress = Task.objects.filter(status="in-progress")
    tasks_done = Task.objects.filter(status="done")

    context = {
        "tasks_todo": tasks_todo,
        "tasks_in_progress": tasks_in_progress,
        "tasks_done": tasks_done,
    }
    return render(request, "task_page.html", context)


def all_categories(request):
    categories = Category.objects.all()
    return render(request, "categories.html", {"categories": categories})


def createcategory(request) :
    context = {}
    form = Create_Category(request.POST or None)
    if form.is_valid() :
        form.save()

    context['form'] = form
    return render(request, "createcategory.html", context)

def category_view(request) :
    context = {}
    context['category'] = Category.objects.all()
    return render(request, "categories.html", context)

def createtask(request) :
    context = {}
    form = Create_Task(request.POST or None)
    if form.is_valid() :
        form.save()
    context['form'] = form
    return render(request, "createtask.html", context)

class TaskDetailView(View):
    form_class = TaskUpdateForm

    def get(self, request, task_id):
        task = Task.objects.get(pk=task_id)
        form = self.form_class(instance=task)
        return render(request, "task.html", {"task": task, "form": form})

    def post(self, request, task_id):
        task = Task.objects.get(pk=task_id)
        if "tag_submit" in request.POST:
            label = request.POST.get("tag")
            if not Tag.objects.filter(label=label).exists():
                Tag.objects.create(label=label)
            tag = Tag.objects.get(label=label)
            task.tags.add(tag)

            return redirect("task", task_id=task_id)

        if "update_submit" in request.POST:
            form = self.form_class(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect("task", task_id=task_id)
            return render(request, "task.html", {"form": form})
