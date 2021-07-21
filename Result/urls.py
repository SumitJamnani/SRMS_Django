from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_result, name='add'),
    path('student_result/', views.student_result, name='student_result'),
    path('reports/', views.reports, name='reports'),
]
