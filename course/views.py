# course/views.py
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

@api_view(['GET'])
def get_courses(request):
    courses = Course.objects.all()
    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_course_detail(request, slug):
    course_detail = Course.objects.get(slug=slug)
    course_detail_serializer = CourseDetailSerializer(course_detail)
    lesson_serializer = LessonListSerializer(course_detail.lessons.all(), many=True)
    
    data = {
        'course_detail': course_detail_serializer.data,    
        'lessons': lesson_serializer.data,    
    }
    
    return Response(data)
