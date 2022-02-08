from pyexpat import model
from sqlite3 import Timestamp
from django.db import models


# Create your models here.

class Contact(models.Model):
    SNo=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    phone=models.CharField(max_length=100)
    content=models.TextField()
    Timestamp=models.DateTimeField(auto_now_add=True, blank=True)