from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.

def rapport(request):
    return render(request, "rapport/rapport.html")

def show(request):
    context = {
        'title': 'The blaclist',
        'Article' : 'abrabrakatabra'
    }
