from django.db import models

# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=200,null=False)
    author = models.CharField(max_length=100,null=False)
    stock = models.PositiveIntegerField(null=False)
    price = models.PositiveIntegerField(null=False)
    date_first_available = models.DateTimeField(auto_now_add=True)