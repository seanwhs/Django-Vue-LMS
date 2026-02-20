# course/views.py
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
    print(request.data)
    
    course = Course.objects.create(
        title=request.data.get('title'),
        slug =slugify(request.data.get('title')),
        short_description=request.data.get("short_description"),
        long_description=request.data.get("long_description"),
        created_by = request.user,
    )
    
    for id in request.data.get('categories'):
        course.categories.add(id)
        
    course.save()
    
    return Response({'yo':'yo'})

@api_view(["GET"])
@permission_classes([AllowAny])
def get_author_courses(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    courses = user.courses.all()
    
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
    courses = Course.objects.all()

    if category_id:
        courses = courses.filter(categories__in=[int(category_id)])

    serializer = CourseListSerializer(courses, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_frontpage_courses(request):
    courses = Course.objects.all()[0:4]
    serializer = CourseListSerializer(courses, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_course_detail(request, slug):
    course_detail = get_object_or_404(Course, slug=slug)
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
