"""
archivos de urls
"""

from django.urls import path, include, re_path
from . import views

app_name="home_app"

urlpatterns=[ 
    path('index', views.IndexView.as_view(),name="index"),
    path('libros',views.listaLibros.as_view(),name="lista")
]
