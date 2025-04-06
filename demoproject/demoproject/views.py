from django.http import HttpResponse 
from django.shortcuts import render

def home(request):
    return HttpResponse("AWS S02 DA Section") 

def about(request):
    return HttpResponse("About page") 

def demo(request):
    return HttpResponse("Welcome page") 

def test(request):
    return render(request,"index.html") 
