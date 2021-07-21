from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_exam, name='add'),
    path('update/', views.update_exam, name='update'),
    path('delete/<int:id>', views.delete_exam, name='delete/'),
    path('search/<int:id>', views.search_exam, name='search/'),
]
