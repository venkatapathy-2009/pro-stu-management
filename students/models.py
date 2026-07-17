from django.db import models
class student(models.Model):
    idi=models.IntegerField(unique=True)
    name=models.CharField(max_length=100)
    roll_no=models.IntegerField(unique=True)
    email=models.EmailField(unique=True)
      

# Create your models here.
