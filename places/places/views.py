from .models import Measurement, Place
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json

def PlaceList(request):
    queryset = Place.objects.all()
    context = list(queryset.values('id', 'name'))
    return JsonResponse(context, safe=False)

def PlaceCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        place = Place()
        place.name = data_json['name']
        place.save()
        return HttpResponse("successfully created place")

def verificar_place(request, place_id):
 
    try:
        place = Place.objects.get(pk=place_id)
        return JsonResponse({'status': 'exists', 'place': {'id': place.id, 'name': place.name, 'location': place.location}}, status=200)
    except Place.DoesNotExist:
        return JsonResponse({'status': 'not_found'}, status=404)
