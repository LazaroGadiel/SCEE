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
	list_display=('nombre','descripcion')
	search_fields=('nombre','descripcion')
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

class EvaluacionAdmin(admin.ModelAdmin):
	list_display=('trabajador','nota','fecha','categoria')
	search_fields=('trabajador','nota','fecha','categoria')
#	list_filter=('name','plaza','fijo','celular','uo','cargo')
admin.site.register(Evaluacion,EvaluacionAdmin)

class Criterio_TrabajadorAdmin(admin.ModelAdmin):
	list_display=('trabajador','criterio','fecha')
	search_fields=('trabajador','criterio','fecha')
#	list_filter=('name','plaza','fijo','celular','uo','cargo')
admin.site.register(Criterio_Trabajador,Criterio_TrabajadorAdmin)

class Logros_FortalezaAdmin(admin.ModelAdmin):
	list_display=('trabajador','descripcion','fecha')
	search_fields=('trabajador','descripcion','fecha')
#	list_filter=('name','plaza','fijo','celular','uo','cargo')
admin.site.register(Logros_Fortaleza,Logros_FortalezaAdmin)

class Deficiencias_DebilidadesAdmin(admin.ModelAdmin):
	list_display=('trabajador','descripcion','fecha')
	search_fields=('trabajador','descripcion','fecha')
#	list_filter=('name','plaza','fijo','celular','uo','cargo')
admin.site.register(Deficiencias_Debilidades,Deficiencias_DebilidadesAdmin)

class RecomendacionesAdmin(admin.ModelAdmin):
	list_display=('trabajador','descripcion','fecha','evidencia')
	search_fields=('trabajador','descripcion','fecha','evidencia')
#	list_filter=('name','plaza','fijo','celular','uo','cargo')
admin.site.register(Recomendaciones,RecomendacionesAdmin)

class TareasAdmin(admin.ModelAdmin):
	list_display=('trabajador','descripcion','fecha_cumplimiento','estado')
	search_fields=('trabajador','descripcion','fecha_cumplimiento','estado')
#	list_filter=('name','plaza','fijo','celular','uo','cargo')
admin.site.register(Tareas,TareasAdmin)

class Plan_FormacionAdmin(admin.ModelAdmin):
	list_display=('trabajador','descripcion','fecha_cumplimiento','estado')
	search_fields=('trabajador','descripcion','fecha_cumplimiento','estado')
#	list_filter=('name','plaza','fijo','celular','uo','cargo')
admin.site.register(Plan_Formacion,Plan_FormacionAdmin)
