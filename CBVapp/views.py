from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CourseSerializer, Course
from rest_framework import status
from django.http import Http404
# Create your views here.

class CourseListView(APIView):
    def get(self, request):
        courses=Course.objects.all()
        serializer=CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=CourseSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Record Added', 'data':serializer.data})
        else:
            return Response(serializer.errors)
        

class CourseDetailsView(APIView):
    def get_course(self, pk):
        try:
            course=Course.objects.get(pk=pk)
            return course
        except Course.DoesNotExist:
            raise Http404



    def get(self, request, pk):
        course=self.get_course(pk)
        serializer=CourseSerializer(course)
        return Response(serializer.data)

    def delete(self, request, pk):
        course=self.get_course(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        course=self.get_course(pk)
        serializer=CourseSerializer(course, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Updated', 'data':serializer.data})
        else:
            return Response(serializer.errors)
    
    
