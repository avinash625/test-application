from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader

from olx.models import *
# Create your views here.

def postlistview(request):
    posts = Post.objects.all();
    template = loader.get_template('plistview.html')
    result = template.render(context = {'posts':posts})
    return HttpResponse(result)

def singlepostview(request,id):
    post = Post.objects.filter(id = id)
    template = loader.get_template("spostview.html")
    result = template.render(context ={"post":post})
    return HttpResponse(result)



