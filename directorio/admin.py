from django.contrib import admin
from .models import *
# Register your models here.

class TrabajadorAdmin(admin.ModelAdmin):
	list_display=('centro','nombre','plaza','cargo','categoria','anexo')
	search_fields=('centro','nombre','plaza','cargo','categoria','anexo')
#	list_filter=('name','plaza','fijo','celular','uo','cargo')
admin.site.register(Trabajador,TrabajadorAdmin)

class Division_TerritorialAdmin(admin.ModelAdmin):
	list_display=['nombre']
	search_fields=['nombre']
#	list_filter=('name','plaza','fijo','celular','uo','cargo')
admin.site.register(Division_Territorial,Division_TerritorialAdmin)

class CentroAdmin(admin.ModelAdmin):
	list_display=('nombre','division_territorial')
	search_fields=('nombre','division_territorial')
#	list_filter=('name','plaza','fijo','celular','uo','cargo')
admin.site.register(Centro,CentroAdmin)

class AspectoAdmin(admin.ModelAdmin):
	list_display=['nombre']
	search_fields=['nombre']
#	list_filter=('name','plaza','fijo','celular','uo','cargo')
admin.site.register(Aspecto,AspectoAdmin)

class AnexoAdmin(admin.ModelAdmin):
	list_display=('nombre','descripcion')
	search_fields=('nombre','descripcion')
#	list_filter=('name','plaza','fijo','celular','uo','cargo')
admin.site.register(Anexo,AnexoAdmin)

class CriterioAdmin(admin.ModelAdmin):
	list_display=('aspecto','valoracion','peso','descripcion')
	search_fields=('aspecto','valoracion','peso','descripcion')
#	list_filter=('name','plaza','fijo','celular','uo','cargo')
admin.site.register(Criterio,CriterioAdmin)
