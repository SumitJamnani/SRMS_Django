from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_semester, name='add'),
    path('update/', views.update_semester, name='update'),
    path('delete/<int:id>', views.delete_semester, name='delete/'),
    path('search/<int:id>', views.search_semester, name='search/'),
]
