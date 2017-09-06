from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.utils import timezone
import datetime
from . models import Libro


def root(request):
    """funcion root que muestra Index page, es la funcion para nuestra pagina de inicio"""
    return HttpResponse("Index Page")

def hello(request):
    """funcion hello que muestra hello world"""
    hello = ("Hello World")
    return render(request, 'library/hello.html', {'hello_world': hello})

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
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            libros = Libro.objects.filter(titulo__icontains=q)
            return render(request, 'library/resultados.html',
                {'libros': libros, 'query': q})
    return render(request, 'library/formulario_buscar.html',
        {'error': error})
