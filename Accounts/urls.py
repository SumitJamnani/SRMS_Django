from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('add_user/', views.register, name='add_user'),
    path('about_us/', views.about_us, name='about_us'),
    path('logout/', views.logout_view, name='logout'),
]
