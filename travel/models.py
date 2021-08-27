from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Destination(models.Model): 
    name = models.CharField(max_length= 50)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default= False)
