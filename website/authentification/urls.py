from django.urls import path
from .views import login


app_name = 'authentification'
urlpatterns = [
    path('', login, name= 'login'),
]