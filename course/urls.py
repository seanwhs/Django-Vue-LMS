# course/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', get_courses, name='get-courses'), 
    path('get_frontpage_courses/', get_frontpage_courses, name='get-frontpage-courses'), 
    path('get_categories/', get_categories, name='get-categories'), 
    path('get_author_courses/<int:user_id>/', get_author_courses, name='get-author-courses'), 
    path('create_course/', create_course, name='create-course'), 
    path('<slug:slug>/', get_course_detail, name='get-course-detail'), 
    path('<slug:course_slug>/<slug:lesson_slug>/', add_comment, name='add-comment'), 
    path('<slug:course_slug>/<slug:lesson_slug>/get-comments/', get_comments, name='get-comments'), 
    path('<slug:course_slug>/<slug:lesson_slug>/get-quiz/', get_quiz, name='get-quiz'), 
]
