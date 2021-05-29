from django.shortcuts import render

# Create your views here.

def import_result_view(request):
	return render(request, 'import_result.html', {})