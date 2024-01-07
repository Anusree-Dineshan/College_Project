from django.http import HttpResponse
from django.shortcuts import render
from . models import Course

# Create your views here.

def demo(request):
    obj=Course.objects.all()
    return render(request,"index.html",{'result':obj})

def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")


