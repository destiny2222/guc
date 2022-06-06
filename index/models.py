from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


# class Publication(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=7, decimal_places=2)
#     dollar_price = models.FloatField(null=True, blank=True)
#     image = models.FileField()
#     slug = models.SlugField(default='', null=True, blank=True)

#     def __str__(self):
#         return self.name

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super(Publication, self).save(*args, **kwargs)

# class ShippingAddress(models.Model):
#     book = models.ForeignKey(Publication, related_name='bookname', on_delete=models.CASCADE)
#     name= models.CharField(max_length=150)
#     email= models.EmailField()
#     phone = models.CharField(max_length= 20)
#     quantity = models.IntegerField(default=1)
#     address = models.CharField(default='enter address',max_length = 150)
   
#     def __str__(self):
#         return f'{self.book} {self.fullname}'        
        


# class Blog(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=7, decimal_places=2)
#     dollar_price = models.FloatField(null=True, blank=True)
#     image = models.FileField()

#     def __str__(self):
#         return self.title        
       