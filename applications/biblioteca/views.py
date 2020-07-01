from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.views.generic import( TemplateView,ListView, )
from .models import Autor, Libros



class listaAutores(ListView):
    template_name='biblioteca/lista_autores.html'
    model=Autor
    context_object_name='autores'