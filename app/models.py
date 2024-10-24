from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    city=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    course_name=models.CharField(max_length=100)
    price=models.IntegerField()
    Duration=models.IntegerField()
    author=models.CharField(max_length=100)

    def __str__(self):
        return self.course_name