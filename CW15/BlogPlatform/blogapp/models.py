from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=255,null=False)
    content=models.CharField(max_length=255,null=False)
    author=models.CharField(max_length=255,null=False)
    publication_date=models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class Category(models.Model):
    name=models.CharField(max_length=255,)
    description=models.TextField()

    def __str__(self) -> str:
        return self.name

class Comment(models.Model):
    post=models.CharField(max_length=255)
    author=models.CharField(max_length=255,null=False)
    content=models.CharField(max_length=255)
    date=models.DateField(auto_now_add=False)

    def __str__(self) -> str:
        return self.post