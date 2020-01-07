from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h2>My first challenge")

def polls(request):
    return HttpResponse("<em>Hello world, you're at polls route.</em>")
