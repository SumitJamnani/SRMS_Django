from django.shortcuts import render

# Create your views here.

def course_mgmt_view(request):
	return render(request, 'course_mgmt.html', {})