from django.urls import path
from . import views
urlpatterns = [
    path('', views.read_about, name='about')
]