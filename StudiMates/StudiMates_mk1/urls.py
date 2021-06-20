"""StudiMates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from . import views
urlpatterns = [
    
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('syllabus',views.syllabus,name='syllabus'),
    path('resources',views.resources,name='resources'),
    path('notes',views.notes,name='notes'),
    path('contact',views.contact,name='contact'),
    path('Qpapers',views.Qpapers,name='Qpapers'),
    path('extras',views.extras,name='extras'),


    #ADded new here on 20 june if getting errors remove this
    path('writtenNotes',views.writtenNotes,name='writtenNotes'),
    path('studilinks',views.studilinks,name='studilinks'),
    path('quetionPapers',views.quetionPapers,name='quetionPapers'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('about',views.about,name='about')






]
