from django.contrib import admin
from . models import Editor, Autor, Libro

# Register your models here.

class AutorAdmin(admin.ModelAdmin):
    #list_display genera en forma de lista los datos que queremos ver en el panel de admin
    list_display = ('nombre', 'apellidos', 'email')
    # search_fields es un buscador y podemos especificar por que podemos buscar
    search_fields = ('nombre', 'apellidos')

class EditorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'domicilio', 'ciudad', 'website')
    search_fields = ('nombre', 'domicilio')

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editor', 'fecha_publicacion')
    list_filter = ('fecha_publicacion',)
    #date_hierarchy añade una lista para poder filtrar por fecha_publicación
    date_hierarchy = 'fecha_publicacion'
    #ordenamos en orden descendente con -
    ordering = ('-fecha_publicacion',)
    #creando fields, indicamos el orden para mostrar el formulario de libros
    #fields = ('titulo', 'autores', 'editor', 'fecha_publicacion')
    #el filtro solo puede aplicarse a campos ManyToManyField
    filter_vertical = ('autores',)
    #buscador de editores dentro de la creación de un libro
    raw_id_fields = ('editor',)

admin.site.register(Editor, EditorAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)