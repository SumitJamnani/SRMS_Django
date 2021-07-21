from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_batch, name='add'),
    path('update/', views.update_batch, name='update'),
    path('delete/<int:id>', views.delete_batch, name='delete/'),
    path('search/<int:id>', views.search_batch, name='search/'),
    path('batch_semester_update/', views.batch_semester_update, name='batch_semester_update'),
]
