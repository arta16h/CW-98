from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView
from django.views import View
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.db.models import Q
from .models import Task, Category, Tag, Create_Category,Create_Task
from .forms import TaskUpdateForm


class HomeView(ListView):
    model = Task
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_list = Task.objects.filter(Q(status__contains="in-progress"))
        page = self.request.GET.get("page")
        tasks = Paginator(task_list, 4).get_page(page)
        context["tasks"] = tasks
        return context


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


def createcategory(request) :
    context = {}
    form = Create_Category(request.POST or None)
    if form.is_valid() :
        form.save()

    context['form'] = form
    return render(request, "createcategory.html", context)


class CategoriesView(ListView):
    model = Category
    template_name = "categories.html"
    context_object_name = "categories"

    def post(self, request):
        name = request.POST.get("category_name")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        Category.objects.create(name=name, description=description, image=image)
        return redirect("categories")


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

class TaskUpdateView(View):
    def post(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs['pk'])
        title = request.POST.get('title')
        description = request.POST.get('description')
        tags = request.POST.get('tag')
        tags_list = []
        try:
            for tag in tags:
                tags_list.append(Tag.objects.get(id=tag))
        except:
            pass
        category = request.POST.get('category')
        due_date = request.POST.get('due_date')
        status = request.POST.get('status')
        file = request.POST.get('file')

        if title:
            task.title = title
        if description:
            task.description = description
        if tags_list:
            task.tags.set(tags_list)
        if category != "none":
            task.category = Category.objects.get(id=category)
        if due_date:
            task.due_date = due_date
        if status != "none":
            task.status = status

        task.save()

        # history = update_cookie(request)
        response = redirect('task_detail', kwargs['pk'])
        # response.set_cookie('history', json.dumps(history))

        return response
