from django.shortcuts import render

# Create your views here.

def director_view(request):
	return render(request, 'director_panel.html', {})