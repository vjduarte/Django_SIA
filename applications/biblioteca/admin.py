from django.contrib import admin

# Register your models here.
from .models import Libros
from .models import Autor

#clase para mejorar el administrador de autor
class AutorAdmin(admin.ModelAdmin):
    list_display=(
        'nombre',
        'nacionalidad',
        'id'
    )
#Atributo para buscar por campo
    search_fields=('nombre','nacionalidad',)

class LibroAdmin(admin.ModelAdmin):
    list_display=(
        'title',
        'resumen',
        'autor',
        'id'
    )
#Atributo para buscar por campo
    search_fields=('title',)
    #para hacer filtros
    list_filter=('autor',)

admin.site.register(Autor,AutorAdmin)
admin.site.register(Libros,LibroAdmin)
