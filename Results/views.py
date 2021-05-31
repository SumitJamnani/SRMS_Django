from django.shortcuts import render

# Create your views here.

def import_result_view(request):
	return render(request, 'import_result.html', {})

def report_view(request):
	return render(request, 'report.html', {})

def student_result_view(request):
	return render(request, 'student_result.html', {})