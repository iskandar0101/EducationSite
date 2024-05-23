from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import ContactPageForm
from .models import CoursePost , TeachersPost, ReviewPost , Plan
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



class CourseDetail(View):
    def get(self, request, pk):
        course = get_object_or_404(CoursePost, pk=pk)
        context = {
            'course': course
        }
        return render(request, 'course_detail.html', context)
   
   
   
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
        return render(request=request , context=context, template_name='review.html')  
    
    
  
class Price(View):
    def get(self, request):
        plans = Plan.objects.all()
        return render(request, 'price.html', {'plans': plans})



class contact(View):
    def get(self, request):
        form = ContactPageForm()
        
        context = {
            'form':form
        }
        return render(request=request, context=context , template_name='contact.html')    
    
    def post(self , request):
        if request.method == 'POST':
            form = ContactPageForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('contact')
    
        return render(request=request, context={'form':form} , template_name='contact.html')    
    
    
    
    
    
    
    
    
    
    
    