# course/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', get_courses, name='get-courses'), 
    path('<slug:slug>/', get_course_detail, name='get-course-detail'), 
]
