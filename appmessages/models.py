import email
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.


class Register(models.Model):
    name = models.CharField(max_length=20)
    email =  models.EmailField()
    address =models.CharField(max_length=20)
    mobile_no = models.IntegerField()