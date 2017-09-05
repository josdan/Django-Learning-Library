from django.conf.urls import url
from . views import root, hello, date, date_next


urlpatterns = [
    #ruta por defecto raiz, seria nuestro index
    url(r'^$', root),

    #añade a la ruta /hello/ la funcion hello de views
    url(r'^hello/$', hello),

    #añade a la ruta /time/ la funcion date de views que devuelve la fecha y hora
    url(r'^time/$', date),

    #añade la ruta /time/more/ y acepta 2 numeros, que es el numero de horas que suma la funcion date_next(offset)
    url(r'^time/more/(\d{1,2})/$', date_next),

]