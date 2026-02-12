# course/views.py
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *


@api_view(["GET"])
def get_courses(request):
    courses = Course.objects.all()
    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_course_detail(request, slug):
    course_detail = Course.objects.get(slug=slug)
    course_detail_serializer = CourseDetailSerializer(course_detail)
    lesson_serializer = LessonListSerializer(course_detail.lessons.all(), many=True)

    data = {
        "course_detail": course_detail_serializer.data,
        "lessons": lesson_serializer.data,
    }

    return Response(data)


@api_view(["GET"])
def get_comments(request, course_slug, lesson_slug):
    lesson = Lesson.objects.get(slug=lesson_slug)
    serializer = CommentsSerializer(lesson.comments.all(), many=True)
    return Response(serializer.data)

@api_view(["POST"])
def add_comment(request, course_slug, lesson_slug):
    data = request.data
    name = data.get("name")
    content = data.get("content")

    course = Course.objects.get(slug=course_slug)
    lesson = Lesson.objects.get(slug=lesson_slug)

    comment = Comment.objects.create(
        course=course,
        lesson=lesson,
        name=name,
        content=content,
        created_by=request.user,
    )

    return Response({'message': 'Comment added successfully!'})