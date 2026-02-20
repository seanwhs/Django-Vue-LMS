# course/views.py
from random import randint
from uuid import uuid4

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.utils.text import slugify

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import *
from .serializers import *

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_course(request):
    
    status = request.data.get('status')
    if status == 'published':
        status = 'draft'
    
    course = Course.objects.create(
        title=request.data.get('title'),
        slug = f"{slugify(request.data.get('title'))}-{uuid4().hex[:6]}",
        short_description=request.data.get("short_description"),
        long_description=request.data.get("long_description"),
        status = status,
        created_by = request.user,
    )
    
    for id in request.data.get('categories'):
        course.categories.add(id)
        
    course.save()
    
    for lesson in request.data.get('lessons', []):
        title = lesson.get('title')

        if not title:
            continue  # Skip empty lessons

        Lesson.objects.create(
            course=course,
            title=title,
            slug=f"{slugify(title)}-{uuid4().hex[:6]}",
            short_description=lesson.get("short_description"),
            long_description=lesson.get("long_description"),
            status=Lesson.DRAFT,
        )
            
    return Response({'course_id':course.id})

@api_view(["GET"])
@permission_classes([AllowAny])
def get_author_courses(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    courses = user.courses.filter(status = Course.PUBLISHED)
    
    user_serializer = UserSerializer(user, many=False)
    courses_serializer = CourseListSerializer(courses, many=True, context={'request': request})    
    
    return Response({
        'courses':courses_serializer.data,
        'created_by': user_serializer.data
    })

@api_view(["GET"])
@permission_classes([AllowAny])
def get_quiz(request, course_slug, lesson_slug):
    lesson = get_object_or_404(Lesson, slug=lesson_slug)
    quiz = lesson.quizzes.first()
    serializer = QuizSerializer(quiz)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([AllowAny])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_courses(request):
    category_id = request.GET.get("category_id", "")
    courses = Course.objects.filter(status = Course.PUBLISHED)

    if category_id:
        courses = courses.filter(categories__in=[int(category_id)])

    serializer = CourseListSerializer(courses, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_frontpage_courses(request):
    courses = Course.objects.filter(status = Course.PUBLISHED)[0:4]
    serializer = CourseListSerializer(courses, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_course_detail(request, slug):
    course_detail = Course.objects.filter(status = Course.PUBLISHED).get(slug=slug)
    lesson_serializer = LessonListSerializer(course_detail.lessons.all(), many=True, context={'request': request})

    # Filter lessons for unauthenticated users
    lessons = lesson_serializer.data
    if not request.user.is_authenticated:
        for lesson in lessons:
            lesson.pop("long_description", None)  # remove it

    course_detail_data = (
        CourseDetailSerializer(course_detail).data
        if request.user.is_authenticated
        else {"title": course_detail.title, "slug": course_detail.slug}  # minimal info
    )

    return Response({
        "course_detail": course_detail_data,
        "lessons": lessons,
    })


@api_view(["GET"])
@permission_classes([AllowAny])
def get_comments(request, course_slug, lesson_slug):
    lesson = Lesson.objects.get(slug=lesson_slug)
    serializer = CommentsSerializer(lesson.comments.all(), many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_comment(request, course_slug, lesson_slug):
    data = request.data

    course = Course.objects.get(slug=course_slug)
    lesson = Lesson.objects.get(slug=lesson_slug)

    comment = Comment.objects.create(
        course=course,
        lesson=lesson,
        name=data.get("name"),
        content=data.get("content"),
        created_by=request.user,
    )

    serializer = CommentsSerializer(comment)

    return Response(serializer.data)
