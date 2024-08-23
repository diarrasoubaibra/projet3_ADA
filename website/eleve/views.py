from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.

def eleve(request):
    return render(request, "eleve/eleve.html")

def ajout_eleve(request):
    return render(request, "eleve/ajout_eleve.html")

def modifier_eleve(request):
    return render(request, "eleve/modifier_eleve.html")

def show(request):
    context = {
        'title': 'The blaclist',
        'Article' : 'abrabrakatabra'
    }
