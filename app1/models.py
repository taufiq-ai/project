from django.db import models

# Create your models here.
class Course(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    