from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    # def __str__(self):
    #     return self.name

    class Meta:
        verbose_name_plural = "Contact Me"

    def __str__(self):
        return self.name + "-" +  self.email     

