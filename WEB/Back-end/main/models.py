from django.db import models

# Create your models here.

class Post(models.Model):
    postname = models.CharField(max_length=50)
    mainphoto = models.ImageField(blank=True, null=True)
    contents = models.TextField()

    def __str__(self):
        return self.postname

class User(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=30)
    categories = models.CharField(max_length=10, default="000") # back-front-ai, 000 ~ 111