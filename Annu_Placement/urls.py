"""Annu_Placement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.dom.expatbuilder import DOCUMENT_NODE
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from Annu_Placement import views
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),

    path('admin/', admin.site.urls),

    path('', views.home ,name='home'),

    path('searchview/', views.searchview ,name='searchview'),

    path('about-us/', views.about,name='about-us'),

    path('jobs/', views.jobs,name='jobs'),

    path('jobsdetails/<job_id>', views.jobsdetails,name='jobsdetails'),

    path('contact/', views.contact,name='contact-us'),

    path('thanks/', views.thanks,name='thanks'),

    path('cv_feedback/', views.cv_feedback),
    
    path('privacyPolicy/', views.privacyPolicy,name='privacyPolicy'),

    path('terms_conditions/', views.terms_conditions,name='terms_conditions'),
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)