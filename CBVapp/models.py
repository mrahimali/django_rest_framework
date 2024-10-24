from django.db import models
from rest_framework import serializers

# Create your models here.

class Course(models.Model):
    course_name=models.CharField(max_length=100)
    price=models.IntegerField()
    Duration=models.IntegerField()
    author=models.CharField(max_length=100)

    def __str__(self):
        return self.course_name
    

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'

