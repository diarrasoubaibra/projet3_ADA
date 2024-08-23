from django.urls import path
from .views import *

app_name = 'professeur'

urlpatterns = [
    path('', professeur, name= 'index'),
    path('ajout_professeur', ajout_prof, name= 'ajout_prof'),
    path('modifier_professeur', modifier_prof, name= 'modifier_prof'),
]