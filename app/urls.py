from django.urls import path
from .views import *
urlpatterns = [
    path('employee/', employeeListView, name='employee_list'),
    path('employee/<int:pk>', employeeDetailView, name='employee_list'),
    path('courses/', course_list, name='course_list'),
    path('courses/<int:pk>', course_details, name='course_list'),
    path('user/', userList, name='user_list'),
]
