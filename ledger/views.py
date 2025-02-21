from django.shortcuts import render, HttpResponse
from django.template import loader

# Create your views here.

def recipebook(request):
    return render(request, "recipebook.html")
