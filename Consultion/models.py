from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Consultion(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

        


      
       