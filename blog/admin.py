from django.contrib import admin
from .models import CoursePost, TeachersPost,ReviewPost

admin.site.register(CoursePost)

admin.site.register(TeachersPost)

admin.site.register(ReviewPost)