from django.db import models

# Create your models here.
class LibraryModel(models.Model):
    rankno=models.IntegerField()
    bname=models.CharField(max_length=300)
    author=models.CharField(max_length=300)
    type=models.CharField(max_length=100)
    
