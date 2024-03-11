# Create your models here.
from django.db import models

# Create your models here.
class User(models.Model):
    Id = models.AutoField(primary_key=True)
    Email = models.CharField(max_length=50)
    Password = models.CharField(max_length=20)