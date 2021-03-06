from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Editor(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=60)
    estado = models.CharField(max_length=30)
    pais = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Editores'

    #si inicializamos un atributo con __str__ despues podemos ver el texto en la shell, por ejemplo: print (Editor.objects.all())
    def __str__(self):
        return self.nombre


class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='e-mail')

    # ordenamos por el atributo nombre
    #hacemos que autor sea plural con verbose_name_plural
    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Autores'

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellidos)



class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    editor = models.ForeignKey(Editor)
    fecha_publicacion = models.DateField(blank=True, null=True)
    portada = models.ImageField(upload_to='portadas', blank=True)

    def __str__(self):
        return self.titulo