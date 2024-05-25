from django.urls import path
from .views import course, CourseDetail, home, Price, Review, teacher, contact

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('course/', course.as_view(), name='course'),
    path('course/<int:pk>/', CourseDetail.as_view(), name='course_detail'),
    path('price/', Price.as_view(), name='price'),
    path('review/', Review.as_view(), name='review'),
    path('teacher/', teacher.as_view(), name='teacher'),
    path('contact/', contact.as_view(), name='contact')
]

