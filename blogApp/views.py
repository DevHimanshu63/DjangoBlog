import re
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bloghome(request): 
    return render(request,'blog/bloghome.html')

def blogpost(request, slug):
    # return HttpResponse(f"blogpost {slug}")
    return render(request,'blog/blogpost.html')