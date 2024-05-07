from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View

class home(View):
    def get(self, request):
class course(View):
    def get(self, request):
        context = {
            'message': 'Hello, World!'
        }

        return render(request=request, template_name='ho me.html', context=context)