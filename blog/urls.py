from django.urls import path
from .views import  course, home ,price , review, teacher , contact

urlpatterns = [
    path('', view=home.as_view(), name='home'),
    path('course/', view=course.as_view(), name='course'),
    path('price/', view=price.as_view(), name='price'),
    path('review/', view=review.as_view(), name='review'),
    path('teacher/',view=teacher.as_view(), name='teacher'),
    path('contact/', view=contact.as_view(), name='contact')
]
