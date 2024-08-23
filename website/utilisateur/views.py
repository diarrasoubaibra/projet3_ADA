from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.

def utilisateur(request):
    return render(request, "utilisateur/utilisateur.html")

def ajout_utilisateur(request):
    return render(request, "utilisateur/ajout_utilisateur.html")

def modifier_utilisateur(request):
    return render(request, "utilisateur/modifier_utilisateur.html")

def show(request):
    context = {
        'title': 'The blaclist',
        'Article' : 'abrabrakatabra'
    }
