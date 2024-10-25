from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('courses', CourseViewSet, basename='courses')

urlpatterns = [
    # path('courses/', CourseListView.as_view(), name='course_list'),
    # path('courses/<int:pk>', CourseDetailsView.as_view(), name='course_detail'),
    path('', include(router.urls))
]
