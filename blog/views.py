from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from .models import CoursePost , TeachersPost, ReviewPost
class home(View):
    def get(self, request):
        return render(request=request, template_name='home.html')
        
         
class course(View):
    def get(self, request):
        course_objects = CoursePost.objects.all()
        
        context = {
            'course_objects':course_objects
        }  
        return render(request=request, context=context , template_name='course.html')


    
class teacher(View):
    def get(self, request):
        teacher_objects = TeachersPost.objects.all()
        
        context = {
            'teacher_objects':teacher_objects
        }
        return render(request=request ,context=context,  template_name='teacher.html') 
    
    
    
class review(View):
    def get(self, request):
        review_objects = ReviewPost.objects.all()
        
        context = {
            'review_objects':review_objects
        }
        return render(request=request ,context=context, template_name='review.html')  
    
  
  
class price(View):
    def get(self, request):
        
        return render(request=request , template_name='price.html')    
    


class contact(View):
    def get(self, request):
        return render(request=request, template_name='contact.html')      
    
    
    
    
    
    
    
    
    
    
    
    