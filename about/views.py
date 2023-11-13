from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Create your views here.
def read_about(request):
    # return HttpResponse("<p>About Us<p>")
    return render(request, 'about/about.html')

