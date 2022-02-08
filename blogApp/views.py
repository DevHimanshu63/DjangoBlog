import re
from django.http import HttpResponse
from django.shortcuts import render
from blogApp.models import Post
# Create your views here.
def bloghome(request): 
    allpost=Post.objects.all()
    context={'allpost':allpost}
    return render(request,'blog/bloghome.html',context)

def blogpost(request, slug):
    
    return render(request,'blog/blogpost.html')