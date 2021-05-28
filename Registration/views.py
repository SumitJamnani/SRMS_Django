from django.shortcuts import render

# Create your views here.

def registration_view(request):
	return render(request, 'registration.html', {})

