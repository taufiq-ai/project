from django.shortcuts import render
from django.http import HttpResponse
from .models import Course

# Create your views here.
def sample_response(request):
    # return HttpResponse('<h1>This is a sample response from APP1<h1>')
    courses = Course.objects.all()
    context = {
        'author_name': 'Taufiq Khan Tusar',
        'courses': courses
    }
    return render(request, 'app1/index.html', context=context)