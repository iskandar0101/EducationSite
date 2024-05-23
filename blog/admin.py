from django.contrib import admin
from .models import CoursePost, TeachersPost,ReviewPost,ContactPage,Plan

admin.site.register(CoursePost)

admin.site.register(TeachersPost)

admin.site.register(ReviewPost)

admin.site.register(ContactPage)

admin.site.register(Plan)
