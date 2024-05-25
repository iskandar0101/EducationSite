from django.shortcuts import redirect, render
from django.views import View
from django.shortcuts import get_object_or_404
from .forms import ContactPageForm, ReviewForm, CommentForm
from .models import CoursePost, TeachersPost, ReviewPost, Plan, Comment

class home(View):
    def get(self, request):
        return render(request=request, template_name='home.html')

class course(View):
    def get(self, request):
        course_objects = CoursePost.objects.all()
        context = {
            'course_objects': course_objects
        }  
        return render(request=request, context=context, template_name='course.html')

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
            'teacher_objects': teacher_objects
        }
        return render(request=request, context=context, template_name='teacher.html')

class Review(View):
    def get(self, request):
        review_objects = ReviewPost.objects.all()
        review_form = ReviewForm()
        comment_form = CommentForm()
        context = {
            'review_objects': review_objects,
            'review_form': review_form,
            'comment_form': comment_form
        }
        return render(request, 'review.html', context)
    
    def post(self, request):
        if 'submit_review' in request.POST:
            review_form = ReviewForm(request.POST, request.FILES)
            if review_form.is_valid():
                review_form.save()
                return redirect('review')
        elif 'submit_comment' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                review_id = request.POST.get('review_id')
                review = get_object_or_404(ReviewPost, id=review_id)
                comment = comment_form.save(commit=False)
                comment.review = review
                comment.user = request.user
                comment.save()
                return redirect('review')
        review_objects = ReviewPost.objects.all()
        review_form = ReviewForm()
        comment_form = CommentForm()
        context = {
            'review_objects': review_objects,
            'review_form': review_form,
            'comment_form': comment_form
        }
        return render(request, 'review.html', context)

class Price(View):
    def get(self, request):
        plans = Plan.objects.all()
        return render(request, 'price.html', {'plans': plans})

class contact(View):
    def get(self, request):
        form = ContactPageForm()
        context = {
            'form': form
        }
        return render(request=request, context=context, template_name='contact.html')    
    
    def post(self, request):
        form = ContactPageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
        context = {
            'form': form
        }
        return render(request=request, context=context, template_name='contact.html')
