"""SRMS URL Configuration

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
from django.urls import path
from Login.views import login_view
from Registration.views import registration_view,import_user_view,homepage_view
from Admin.views import admin_view
from Director.views import director_view
from Faculty.views import faculty_view
from Student.views import student_view
from Results.views import import_result_view

urlpatterns = [
    path('',login_view, name=''),
    path('admin/', admin_view, name='admin'),
    path('login/',login_view, name='login'),
    path('registration/',registration_view, name='registration'),
    path('base/',admin_view, name='base'),
    path('director/', director_view, name='director'),
    path('faculty/', faculty_view, name='faculty'),
    path('student/', student_view, name='student'),
    path('import_user/', import_user_view, name='import_user'),
    path('home/', homepage_view, name='home'),
    path('import_result/', import_result_view, name='import_result'),
]
