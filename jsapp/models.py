from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length = 200, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.title)

class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    creator = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return str(self.title)
    
