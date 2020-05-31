from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import *


def listado(request):
    lista = serializers.serialize('json', Persona.objects.all(),fields=['id','name','plaza','fijo','celular','cargo','uo'])
    return HttpResponse(lista, content_type='application/json')

def index(request):
    return render(request,'persona/index.html')


@method_decorator(csrf_exempt)
def persona_crear(request):
    json_data = json.loads(request.body)
    form = PersonaForm(json_data)
    if form.is_valid():
            instance=form.save()
            ser_instance=serializers.serialize('json', [instance,])
            return JsonResponse({"instance": ser_instance}, status=200)
    else: 
      return JsonResponse({"error": form.errors}, status=400)
       
    return JsonResponse({"error": form.errors}, status=400)

@method_decorator(csrf_exempt)
def persona_actualizar(request,id_persona):
    data =  dict()
    persona =  Persona.objects.get(id=id_persona)
    json_data = json.loads(request.body)
    form = PersonaForm(instance=persona,data=json_data)
    if form.is_valid():
            instance=form.save()
            data['persona'] = model_to_dict(instance)
            return JsonResponse(data)
    else: 
      return JsonResponse({"error": form.errors}, status=400)
       
    return JsonResponse({"error": form.errors}, status=400)

def persona_detalles(request,id_persona):
    persona =  Persona.objects.get(id=id_persona)
    if request.method=='GET':
        data=dict()
        data['persona']=model_to_dict(persona)
        return JsonResponse(data)  
    return JsonResponse({"error": form.errors}, status=400)

@method_decorator(csrf_exempt)
def persona_delete(request,id_persona):
    persona = Persona.objects.get(id=id_persona)
    data=dict()
    data['persona']=model_to_dict(persona)
    persona.delete()
    return JsonResponse(data)

def listado_solicitud(request):
    data=list(Solicitud.objects.select_related('persona').values('persona__name','id','razones','numero_mascotas'))   
    return HttpResponse(json.dumps(data,cls=DjangoJSONEncoder))

def listado_centro(request):
    data=list(Centro.objects.select_related('persona').values('persona__name','id','nombre'))   
    return HttpResponse(json.dumps(data,cls=DjangoJSONEncoder))

def personas_select2(request):
    data=Persona.objects.values('name','id')   
    return HttpResponse(json.dumps(list(data), cls=DjangoJSONEncoder))    

@method_decorator(csrf_exempt)
def solicitud_crear(request):
    json_data = json.loads(request.body)
    form = SolicitudForm(json_data)
    if form.is_valid():
            instance=form.save()
            ser_instance=serializers.serialize('json', [instance,])
            return JsonResponse({"instance": ser_instance}, status=200)
    else: 
      return JsonResponse({"error": form.errors}, status=400)
       
    return JsonResponse({"error": form.errors}, status=400)

@method_decorator(csrf_exempt)
def solicitud_actualizar(request,id_solicitud):
    data =  dict()
    solicitud =  Solicitud.objects.get(id=id_solicitud)
    json_data = json.loads(request.body)
    form = SolicitudForm(instance=solicitud,data=json_data)
    if form.is_valid():
            instance=form.save()
            data['solicitud'] = model_to_dict(instance)
            return JsonResponse(data)
    else: 
      return JsonResponse({"error": form.errors}, status=400)
       
    return JsonResponse({"error": form.errors}, status=400)

def solicitud_detalles(request,id_solicitud):
    solicitud =  Solicitud.objects.get(id=id_solicitud)
    if request.method=='GET':
        data=dict()
        data['solicitud']=model_to_dict(solicitud)
        return JsonResponse(data)  
    return JsonResponse({"error": form.errors}, status=400)  

@method_decorator(csrf_exempt)
def solicitud_eliminar(request,id_solicitud):
    solicitud = Solicitud.objects.get(id=id_solicitud)
    data=dict()
    data['solicitud']=model_to_dict(solicitud)
    solicitud.delete()
    return JsonResponse(data)      