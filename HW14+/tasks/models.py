from django.db import models
from django import forms

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = (
        ("to-do", "To Do"),
        ("in-progress", "In Progress"),
        ("done", "Done"),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
    
class Create_Category(forms.ModelForm) :
    class Meta :
        model = Category
        fields = [
            "name"
        ]

class Create_Task(forms.ModelForm) :
    class Meta :
        model = Task
        fields = [
            "title",
            "description",
            "due_date",
            "status",
            "category",
            "tags"
        ]

