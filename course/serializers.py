# course/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug')

# course/serializers.py

class CourseListSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(many=False) 
    
    class Meta:
        model = Course
        fields = [
            'id', 
            'title', 
            'slug', 
            'short_description', 
            'long_description', 
            'get_image', 
            'created_by' 
        ]

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        request = self.context.get('request')
        # Check if request exists to avoid errors during certain tests/calls
        if request and not request.user.is_authenticated:
            ret.pop('long_description', None)
            ret.pop('short_description', None)
        return ret


class CourseDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(many=False)
    class Meta:
        model = Course
        fields = ('id', 'title', 'slug', 'short_description', 'long_description', 'created_by', 'get_image')

class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'slug', 'lesson_type', 'short_description', 'long_description', 'youtube_id']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        request = self.context.get('request')
        if not request.user.is_authenticated:
            # Remove sensitive fields
            ret.pop('long_description', None)
            ret.pop('short_description', None)
        return ret

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'name', 'content', 'created_at')
        
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'lesson_id', 'question', 'answer', 'opt1', 'opt2', 'opt3', 'opt4', 'opt5')