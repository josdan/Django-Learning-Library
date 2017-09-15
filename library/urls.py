from django.conf.urls import url
from . views import root, hello, date, date_next, browser, buscar, contactos
from library import views
from library.views import Start




urlpatterns = [
    #ruta por defecto raiz, seria nuestro index
    url(r'^$', root),

    #añade a la ruta /hello/ la funcion hello de views
    url(r'^hello/$', hello),

    #start basado en vistas
    url(r'^start/$', (views.Start.as_view()), name='start'),

    #añade a la ruta /time/ la funcion date de views que devuelve la fecha y hora
    url(r'^time/$', date),

    #añade la ruta /time/more/ y acepta 2 numeros, que es el numero de horas que suma la funcion date_next(offset)
    url(r'^time/more/(\d{1,2})/$', date_next),

    #añade la ruta browser e indica el navegador que estas usando
    url(r'^browser/$', browser),

    #añade la ruta buscar, para cuando pulsemos en buscar dentro de formulario_buscar
    url(r'^buscar/$', buscar),

    #añade la ruta formularios_contactos, es un formulario y envia un mail
    url(r'^contactos/$', contactos),

    #añade la ruta inicio e indice
    url(r'^inicio/$', views.lista_libros),
    url(r'^indice/$', views.lista_editores),

]

