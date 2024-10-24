from rest_framework import serializers
from .models import Employee, Course
from django.contrib.auth.models import User

# request.post -> handle form data. Only works for 'POST' method
# request.data -> handle arbitrary data. works for POST, PUT and PATCH methods


# class EmployeeSerializer(serializers.Serializer):
#     name= serializers.CharField(max_length=100)
#     email=serializers.CharField(max_length=100)
#     phone=serializers.CharField(max_length=10)
#     city=serializers.CharField(max_length=50)

#     def create(self, validated_data):
#         print("Create method called.....")
#         return Employee.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         print("update function running......")
#         newEmployee=Employee(**validated_data)
#         newEmployee.id=instance.id
#         newEmployee.save()
#         return newEmployee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        # fields=['name', 'email']
        fields='__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'

# class UserSerializer(serializers.Serializer):
#     username=serializers.CharField(max_length=50)
#     email=serializers.EmailField()
#     password=serializers.CharField(max_length=200)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

   