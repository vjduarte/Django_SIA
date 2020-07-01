from django.shortcuts import render

# Create your views here.
from django.views.generic import( TemplateView,ListView, )

class IndexView(TemplateView):
    # una vista procesa datos y renderiza el resultado en pantalla
    # un template es un archivo html
    template_name="home/index.html"

class listaLibros(ListView):
    template_name='home/lista.html'
    queryset=['principito','codigo da vinci','xxx']
    context_object_name='libros'
  