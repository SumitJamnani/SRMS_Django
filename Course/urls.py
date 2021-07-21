from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_course, name='add'),
    path('update/<int:id>', views.update_course, name='update/'),
    path('delete/<int:id>', views.delete_course, name='delete/'),
    path('search/<int:id>', views.search_course, name='search/'),
]
