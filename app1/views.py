from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from . forms import CourseEndorse
from django.contrib.auth.forms import UserCreationForm
from django.views import View
# Create your views here.
def sample_response(request):
    # return HttpResponse('<h1>This is a sample response from APP1<h1>')
    course_endorse_form = CourseEndorse()
    courses = Course.objects.all()
    context = {
        'author_name': 'Taufiq Khan Tusar',
        'form' : course_endorse_form,
        'courses': courses
    }
    return render(request, 'app1/index.html', context=context)

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Registration Successful')
    else:
        form = UserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'app1/registration.html', context=context)

class TestView(View):
    def get(self, request):
        return render(request, 'app1/test.html')
    
