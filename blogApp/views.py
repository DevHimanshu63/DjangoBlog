from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bloghome(request): 
    return HttpResponse("bloghome")

def blogpost(request, slug):
    return HttpResponse(f"blogpost {slug}")