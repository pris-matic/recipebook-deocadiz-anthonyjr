from django.shortcuts import render, HttpResponse
from django.template import loader

# Create your views here.

def recipebook(request):
    return HttpResponse("hello world")
