from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, "hello/index.html")
def guizin(request):
	return HttpResponse("Hello, Guizin!")

def greet(request,name):
	return render(request, "greet/greet.html", {
		"name": name.capitalize()
	})
