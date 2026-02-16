# activity/views.py
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from activity.serializers import ActivitySerializer

from .models import *
from course.models import *
from course.serializers import CourseListSerializer
from .serializers import *


@api_view(["GET"])
@permission_classes([IsAuthenticated]) 
def get_active_courses(request):
    courses = []

    for activity in request.user.activities.all():
        if activity.status == activity.STARTED and activity.course not in courses:
            courses.append(activity.course)

    serializer = CourseListSerializer(courses, many=True, context={'request': request})

    return Response(serializer.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated]) 
def track_started(request, course_slug, lesson_slug):
    course = get_object_or_404(Course, slug=course_slug)
    lesson = get_object_or_404(Lesson, slug=lesson_slug)
    
    if Activity.objects.filter(created_by=request.user, course=course, lesson=lesson).count()==0:
        Activity.objects.create(course=course, lesson=lesson, created_by=request.user)
        
    activity = Activity.objects.get(created_by=request.user, course=course, lesson=lesson)
    
    serializer=ActivitySerializer(activity, context={'request': request})
    
    return Response(serializer.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated]) 
def mark_as_done(request, course_slug, lesson_slug):
    course = get_object_or_404(Course, slug=course_slug)
    lesson = get_object_or_404(Lesson, slug=lesson_slug)

    activity = Activity.objects.get(created_by=request.user, course=course, lesson=lesson)
    activity.status = Activity.DONE
    activity.save()
    
    serializer=ActivitySerializer(activity, context={'request': request})
    
    return Response(serializer.data)