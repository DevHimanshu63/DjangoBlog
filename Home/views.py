import re
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home/home.html')
def about(request):
    return HttpResponse("about")
def contact(request):
    return render(request,'home/contact.html')