from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def read_blog(request):
    # return HttpResponse("<p> This is blogging site<p>")
    return render(request, 'blog/blog.html')

