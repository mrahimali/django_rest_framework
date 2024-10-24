from django.shortcuts import render, HttpResponse
# from django.http import JsonResponse
from .models import Employee, Course
from .serializer import EmployeeSerializer, UserSerializer, CourseSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET', 'POST'])
def course_list(request):
    if request.method=='GET':
        courses=Course.objects.all()
        serializer=CourseSerializer(courses, many=True)
        return Response(serializer.data)
    

    elif request.method=='POST':
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return Response({'status':status.HTTP_201_CREATED, 'data':serializer.data})
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET','PUT', 'DELETE'])
def course_details(request, pk):
    try:
        course=Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response({'status':status.HTTP_204_NO_CONTENT, 'message':'No Course Found'})
    
    if request.method=='GET':
        serializer=CourseSerializer(course)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer=CourseSerializer(course, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Updated', 'data':serializer.data})
        else:
            return Response(serializer.errors)
    

    elif request.method=='DELETE':
        course.delete()
        return Response({'message':'Deleted', 'status':status.HTTP_404_NOT_FOUND})


# @csrf_exempt
@api_view(['GET', 'POST'])
def employeeListView(request):
    if request.method=='GET':
        employees=Employee.objects.all()
        serializer=EmployeeSerializer(employees, many=True)
        data=serializer.data
        # return JsonResponse(data, safe=False)
        return Response(data)


    elif request.method=='POST':
        # jsonData=JSONParser().parse(request)

        # serializer=EmployeeSerializer(data=jsonData)
        serializer=EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data, safe=False)
            return Response(serializer.data)
        else:
            # return JsonResponse(serializer.errors, safe=False)
            return Response(serializer.errors)






# @csrf_exempt
@api_view(['GET', 'DELETE','PUT'])
def employeeDetailView(request, pk):
    try:
        employee=Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return HttpResponse(status=404)

    if request.method=='GET':
        
        serializer=EmployeeSerializer(employee)
        data=serializer.data
        # return JsonResponse(data, safe=False)
        return Response(data)
    

    elif request.method=='DELETE':
        employee.delete()
        return HttpResponse(status.HTTP_204_NO_CONTENT)
        
    elif request.method=='PUT':
        # jsonData=JSONParser().parse(request)
        # serializer=EmployeeSerializer(employee,data=jsonData)
        serializer=EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data, safe=False)
            return Response(serializer.data)
        else:
            # return JsonResponse(serializer.errors, safe=False)
            return Response(serializer.errors)



@api_view(['GET'])
def userList(request):
    users=User.objects.all()
    serializer=UserSerializer(users, many=True)
    data=serializer.data
    # return JsonResponse({"users":data}, safe=False)
    return Response(data)