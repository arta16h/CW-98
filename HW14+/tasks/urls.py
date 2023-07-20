from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.search, name="search"),
    path("task/<int:task_id>/", views.task, name="task"),
    path("tasks/", views.task_page, name="task_page"),
    path("categories/", views.all_categories, name="all_categories"),
    path("create_category/", views.createcategory, name="create_category"),
    path("create_task/", views.createtask, name="create_task")
    ]
