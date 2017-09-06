from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect, Http404
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
    errors = []
    if request.method == 'POST':
        if not request.POST.get('asunto', ''):
            errors.append('Por favor introduce el  asunto.')
        if not request.POST.get('mensaje', ''):
            errors.append('Por favor introduce un mensaje.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Por favor introduce una direccion de e-mail valida.')
        if not errors:
            send_mail(
                request.POST['asunto'],
                request.POST['mensaje'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contactos/gracias/')
    return render(request, 'library/formulario_contactos.html',
        {'errors': errors})