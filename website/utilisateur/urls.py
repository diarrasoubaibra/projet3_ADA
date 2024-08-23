from django.urls import path
from .views import *

app_name = 'utilisateur'

urlpatterns = [
    path('', utilisateur, name= 'index'),
    path('add-user-page', ajout_utilisateur, name= 'ajout_utilisateur'),
    path('update-user-page', modifier_utilisateur, name= 'modifier_utilisateur'),
]