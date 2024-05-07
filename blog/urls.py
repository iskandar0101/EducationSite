from django.urls import path
from .views import course

urlpatterns = [

    path('', view=course.as_view(), name='home_page'),
]