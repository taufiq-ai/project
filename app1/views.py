from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from . forms import CourseEndorse
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

def course_endorse(request):
    
    return render(request, 'app1/course_endorse.html')