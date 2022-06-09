from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=200)
    thumb = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CharField)
    body = RichTextField(blank=True, null=True)
    dou = models.CharField(max_length=200, null=True, blank=True)
    tag1 = models.CharField(max_length=500)
    tag2 = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class comment(models.Model):
    blog_post = models.ForeignKey(post, on_delete=models.CASCADE)
    name = models.CharField(max_length=2000, null=True, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.blog_post