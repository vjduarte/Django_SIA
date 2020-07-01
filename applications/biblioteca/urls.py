"""
archivos de urls
"""

from django.urls import path, include, re_path
from . import views

app_name="biblioteca_app"

urlpatterns=[ 
    path('autores',views.listaAutores.as_view(),name="lista_autores")
]
