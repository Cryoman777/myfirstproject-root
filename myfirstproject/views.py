from django.http import HttpResponse
from django.shortcuts import render

def about(request):
	return HttpResponse('This is about page')


def home(request):
	return render(request, 'home.html', {'greeting':'Hello!'})

def ex1(request):
	return render(request, 'ex1.html')