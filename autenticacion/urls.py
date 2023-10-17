from django.urls import path, include, re_path
from .views import VRegistro, cerrar_session, logear
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('', VRegistro.as_view(), name = 'Autenticacion'),
    path('cerrar_sesion', cerrar_session, name = 'cerrar_sesion'),
    path('logear', logear, name = 'logear'),
    
]