from django.urls import path
from .views import *

app_name = 'eleve'

urlpatterns = [
    path('', eleve, name='index'),
    path('ajout_eleve', ajout_eleve, name='ajout_eleve'),
    path('modifier_eleve', modifier_eleve, name='modifier_eleve'),
]