from django.urls import path
from . import views

urlpatterns = [
    path('', views.sample_response, name='home'),
    path('registration', views.registration, name='registration'),
    path('test', views.TestView.as_view(), name='test')
]