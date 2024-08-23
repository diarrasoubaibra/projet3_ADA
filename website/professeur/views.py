from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.

def professeur(request):
    return render(request, "professeur/professeur.html")

def ajout_prof(request):
    return render(request, "professeur/ajout_prof.html")

def modifier_prof(request):
    return render(request, "professeur/modifier_prof.html")

def show(request):
    context = {
        'title': 'The blaclist',
        'Article' : 'abrabrakatabra'
    }
