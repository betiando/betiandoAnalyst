from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	question = 1
	return render(request, 'analyst/home.html', {'question': question})
	
	
	
def data(request):
	return render(request, 'analyst/data.html', {})
