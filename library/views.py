from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import timezone
import datetime
from . models import Libro, Editor
from . forms import FormularioContactos
from django.views.generic import TemplateView


def root(request):
    """funcion root que muestra Index page, es la funcion para nuestra pagina de inicio"""
    return HttpResponse("Index Page")

def hello(request):
    """funcion hello que muestra hello world"""
    hello = ("Hello World")
    return render(request, 'library/hello.html', {'hello_world': hello})

class Start(TemplateView):
    template_name = 'library/start.html'

def date(request):
    """funcion que devuelve la fecha y hora"""
    now = timezone.datetime.now()
    return render(request, 'library/time.html', {'date_now': now})

def date_next(request, offset):
    """captura la fecha y hora actual y le suma las horas que yo ponga(offset)"""
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return HttpResponse(dt)

def browser(request):
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    return HttpResponse("Tu navegador es %s" % ua)





def buscar(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Por favor introduce un termino de busqueda.')
        elif len(q) > 20:
            errors.append('Por favor introduce un termino de busqueda menor a 20 caracteres.')
        else:
            libros = Libro.objects.filter(titulo__icontains=q)
            return render(request, 'library/resultados.html',
                {'libros': libros, 'query': q})
    return render(request, 'library/formulario_buscar.html',
                  {'errors': errors})


def contactos(request):
    if request.method == 'POST':
        form = FormularioContactos(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            send_mail(
                datos['asunto'],
                datos['mensaje'],
                datos.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contactos/gracias/')
    else:
        form = FormularioContactos(initial={'asunto': 'Escribe un titulo'})
    return render(request, 'library/formulario_contactos.html', {'form': form})

def lista_libros(request):
    lista_libros = Libro.objects.all()
    return render(request, 'library/lista_libros.html', {'lista_libros': lista_libros})


def lista_editores(request):
    lista_editores = Editor.objects.all()
    return render(request, 'library/lista_editores.html', {'lista_editores': lista_editores})