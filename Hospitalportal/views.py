# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def index2(request):
    return render(request,'index2.html')

def index3(request):
    return render(request,'index3.html')

def starter(request):
    return render(request,'starter.html')

def iframe(request):
    return render(request,'iframe.html')