import re
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from Home.models import Contact

# Create your views here.
def home(request):
    return render(request,'home/home.html')
def about(request):
    return HttpResponse("about")
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        if len(name)<2 or len(email)<5 or len(phone)<9:
            messages.error(request,"fill the form correctly")
        else:
            user=Contact(Name=name,email=email,phone=phone,content=content)
            user.save()
            messages.success(request,"your message was submitted")
    return render(request,'home/contact.html')