from django.shortcuts import render

# Create your views here.

def student_view(request):
	return render(request, 'student_panel.html', {})