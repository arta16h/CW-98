from django.db import models

#Category Model: Fields: name, description, and any other relevant information.
# o Comment Model: Fields: post, author, content, date, and any other relevant information.

class Post(models.Model):
    title=models.CharField(max_length=255,null=True)
    content=models.CharField(max_length=255,null=True)
    author=models.CharField(max_length=255,null=True)
    publication_date=models.DateField(auto_now_add=True)

class Category(models.Model):
    name=models.CharField(max_length=255,)