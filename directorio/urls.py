from django.urls import *
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    path('nuevo/', login_required(persona_crear), name='persona_crear'),
    path('detalles/<id_persona>/', login_required(persona_detalles), name='persona_detalles'),
    path('actualizar/<id_persona>/', login_required(persona_actualizar), name='persona_actualizar'),
    path('eliminar/<id_persona>/', login_required(persona_delete), name='persona_eliminar'),
    path('listado/', login_required(listado), name='listado'),
    path('listado_solicitud/', login_required(listado_solicitud), name='listado_solicitud'),
    path('solicitud_crear/', login_required(solicitud_crear), name='solicitud_crear'),
    path('personas_select2/', login_required(personas_select2), name='personas_select2'),
    path('solicitud_detalles/<id_solicitud>/', login_required(solicitud_detalles), name='solicitud_detalles'),
    path('solicitud_actualizar/<id_solicitud>/', login_required(solicitud_actualizar), name='solicitud_actualizar'),
    path('solicitud_eliminar/<id_solicitud>/', login_required(solicitud_eliminar), name='solicitud_eliminar'),
    path('listado_centro/', login_required(listado_centro), name='listado_centro'),
]