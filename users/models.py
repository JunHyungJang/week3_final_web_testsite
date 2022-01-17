from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    student_id = models.CharField(max_length = 10)
    # profile_img = models.ImageField(null = True)

class Board(models.Model):
    # author = models.CharField(max_length=10, null=False)
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null = False)
    content = models.TextField(null = False)
    created_date = models.DateTimeField(auto_now_add = True)
    modified_date = models.DateTimeField(auto_now_add = True)
    

