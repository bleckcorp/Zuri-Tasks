from turtle import title
from unicodedata import name
from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model

# Create your models here.

class Post(models.Model):
    title= models.CharField (max_length=200)
    text=models.TextField
    author= get_user_model
    Created_date=models.DateTimeField
    Published_date = models.DateTimeField


