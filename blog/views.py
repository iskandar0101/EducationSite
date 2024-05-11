from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View

class home(View):
    def get(self, request):
        return render(request=request, template_name='home.html')
        
         
class course(View):
    def get(self, request):
        return render(request=request, template_name='course.html')

    
class price(View):
    def get(self, request):
        return render(request=request , template_name='price.html')    
    

class review(View):
    def get(self, request):
        return render(request=request , template_name='review.html')  
    
class teacher(View):
    def get(self, request):
        return render(request=request , template_name='teacher.html')    
    

class contact(View):
    def get(self, request):
        return render(request=request, template_name='contact.html')      
    
    
    
    
    
    
    
    
    
    
    
    