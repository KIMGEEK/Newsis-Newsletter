from django.db import models

# Create your models here.

class Post(models.Model):
    weeks = models.CharField(max_length=30) # "3월 2주차"
    index = models.IntegerField() # 0 ~ 3
    news = models.TextField() # {"date": "2025-05-24", "postname": "Hello world Title", "contents": "Hello world Content"}
    image = models.TextField() # '7JWI64WVpw=='

    def __str__(self):
        return self.weeks

class User(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=30)