from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

class post(models.Model):
    STATUS.CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='published')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_lenght=10, choices=STATUS_CHOICES, default='draft')


 class Meta:
     ordering = ('-publish',)

def __str__(self):
         return self.title
