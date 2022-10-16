from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import BlogPost

# Create your views here.
def BlogHome(request):
    posts=BlogPost.objects.filter(publication=True).order_by('id')
    return render(request, 'posts.html',context={'posts':posts})

def BlogRecette(request,id):
    try:
        post = BlogPost.objects.get(pk=int(id))
    except BlogPost.DoesNotExist:
        raise Http404('Post inexistant')
    return render(request,'post.html',context={'post':post})