from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_division, name='add'),
    path('update/', views.update_division, name='update'),
    path('delete/<int:id>', views.delete_division, name='delete/'),
    path('search/<int:id>', views.search_division, name='search/'),
]
