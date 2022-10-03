from post.models import Feature
from django.shortcuts import render
from .models import Feature


# Create your views here.
def index(request):
    post=Feature.objects.all()
    return render(request,"index.html",{"object_list":post})

def posts(request,pk):
    posts=Feature.objects.get(id=pk)
    return render (request,"posts.html",{"posts":posts})


