from django.shortcuts import render

# Create your views here.

def registration_view(request):
	return render(request, 'registration.html', {})

def import_user_view(request):
	return render(request, 'import_user.html', {})

def homepage_view(request):
	return render(request, 'home.html', {})
