# course/serializers.py
from rest_framework import serializers
from .models import *

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'slug', 'short_description')
