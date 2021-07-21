from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_subject, name='add'),
    path('update/', views.update_subject, name='update'),
    path('delete/<int:id>', views.delete_subject, name='delete/'),
    path('search/<int:id>', views.search_subject, name='search/'),
]
