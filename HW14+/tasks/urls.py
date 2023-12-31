from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("search/", views.search, name="search"),
    path("task/<int:task_id>/", views.TaskDetailView.as_view(), name="task"),
    path("tasks/", views.task_page, name="task_page"),
    path("categories/", views.CategoriesView.as_view(), name="all_categories"),
    path("create_category/", views.createcategory, name="create_category"),
    path("create_task/", views.createtask, name="create_task")
    ]
