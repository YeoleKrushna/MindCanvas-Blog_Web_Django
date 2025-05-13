"""Creating models here so they can interact with databases and views"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    """Category Model for Post Categorization"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    """We have Model here to create Post for Database Creation"""
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='posts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

