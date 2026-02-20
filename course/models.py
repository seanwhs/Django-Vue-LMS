# course/models.py
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title


class Course(models.Model):
    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='courses', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)

    def __str__(self):
        categories_str = ", ".join([c.title for c in self.categories.all()])
        return f'Categories: {categories_str} | Title: {self.title}'
    
    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return "https://placehold.co/1280x960"
        

class Lesson(models.Model):
    DRAFT = 'draft'    
    PUBLISHED = 'published'    
    
    CHOICES_STATUS = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    )
    
    ARTICLE = 'article'
    QUIZ = 'quiz'
    VIDEO = 'video'
    
    CHOICES_LESSON_TYPE = (
        (ARTICLE, 'Article'),
        (QUIZ, 'Quiz'),
        (VIDEO, 'Video'),
    )
    
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices = CHOICES_STATUS, default=PUBLISHED)
    lesson_type = models.CharField(max_length=20, choices = CHOICES_LESSON_TYPE, default=ARTICLE)
    youtube_id = models.CharField(max_length=20, blank=True, null=True)
    
class Comment(models.Model):
    course = models.ForeignKey(Course, related_name='comments', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Comment for: {self.lesson} | By: {self.name}'
    
class Quiz(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='quizzes', on_delete=models.CASCADE)
    question = models.CharField(max_length=255, null=True)
    answer = models.CharField(max_length=255, null=True)
    opt1 = models.CharField(max_length=255, null=True)
    opt2 = models.CharField(max_length=255, null=True)
    opt3 = models.CharField(max_length=255, null=True)
    opt4 = models.CharField(max_length=255, null=True)
    opt5 = models.CharField(max_length=255, null=True)
    
    class Meta:
        verbose_name_plural = 'Quizzes'
