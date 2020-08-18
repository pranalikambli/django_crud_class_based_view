from django.db import models
from django.utils import timezone


class Blogs(models.Model):
    class Meta:
        db_table = 'blogs'

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    excerpt = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, default='draft')
    author = models.CharField(max_length=500)
