# core/urls.py --> main project
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')), # find this urls first
    path('api/v1/', include('djoser.urls.authtoken')), # find this url if previous did not work
    path('api/v1/courses/', include('course.urls')), 
]
