from django.shortcuts import render, redirect
# Importo estos tres modulos
from .models import Personaje
from django.http import HttpResponse
from django.template import loader
from .forms import PersonajeForm
#from django import forms

# Create your views here.
def personajes(request):
    personajes_list = Personaje.objects.all()
    template = loader.get_template("personajes.html")
    context = { "personajes_list": personajes_list}
    return HttpResponse(template.render(context, request))

"""def personaje_form (request):
    if request.method == "POST":
        form=PersonajeForm (request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Personajes')
        else:
            form= PersonajeForm()
            context={'form':form}
            return render(request,"carga_persona.html", context)"""
        
def personaje_form(request):
    context = {'form': PersonajeForm() }
    if request.method == "POST":
        form = PersonajeForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save() 
            context["mensaje"] = "Se guardo el form"
            return redirect("pj:personajes")
        else:
            context["mensaje"] = "No se guardo el form"
            context["form"] = form
    
    return render(request, "carga_persona.html", context)