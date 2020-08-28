from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=30)
    id=models.IntegerField(default=0,primary_key=True)
    contact=models.IntegerField(default=0)
    address=models.CharField(max_length=50)