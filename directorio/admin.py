from django.contrib import admin
from .models import *
# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
	list_display=('name','plaza','fijo','celular','uo','cargo')
	search_fields=('name','plaza','fijo','celular','uo','cargo')
#	list_filter=('name','plaza','fijo','celular','uo','cargo')
admin.site.register(Persona,PersonaAdmin)

class SolicitudAdmin(admin.ModelAdmin):
	list_display=('persona','numero_mascotas','razones')
	search_fields=('persona','numero_mascotas','razones')
#	list_filter=('name','plaza','fijo','celular','uo','cargo')
admin.site.register(Solicitud,SolicitudAdmin)

class CentroAdmin(admin.ModelAdmin):
	list_display=['nombre']
	search_fields=['nombre']
#	list_filter=('name','plaza','fijo','celular','uo','cargo')
admin.site.register(Centro,CentroAdmin)