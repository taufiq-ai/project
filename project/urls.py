"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

### Uncomment when urls not defined inside apps --------------------
# from app1 import views as app1_views
# from blog import views as blog_views
# from about import views as about_views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', app1_views.sample_response),
#     path('blog', blog_views.read_blog),
#     path('about', about_views.read_about),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
    path('blog/', include('blog.urls')),
    path('about/', include('about.urls')),
]
