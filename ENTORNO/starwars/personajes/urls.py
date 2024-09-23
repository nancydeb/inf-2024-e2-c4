from django.urls import path

from . import views
from .views import personaje_form, personajes
from django.urls import path


app_name = 'pj'

urlpatterns = [ 
    path('', personajes, name="personajes"),
    path('carga_personaje/', personaje_form, name="carga_personaje"),
]