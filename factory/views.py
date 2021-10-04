from django.http import HttpResponse
from django.shortcuts import render

from factory.models import Factory
from factory.models import Production
from factory.models import Sprocket


def home(request):
    return HttpResponse('hello')


def get_all_factories(request):
    production = Production.objects.all()
    return HttpResponse(production)


def get_factory(response, id):
    production = Production.objects.filter(factory__id=id)
    return HttpResponse(production)


def get_sprocket(response, id):
    sprocket = Sprocket.objects.get(id=id)
    return HttpResponse(sprocket)

def create_sprocket(response, teeth, pitch_diameter, outside_diameter, pitch):
    sprocket = Sprocket.objects.create(teeth=teeth, pitch_diameter=pitch_diameter, outside_diameter=outside_diameter, pitch=pitch)
    return HttpResponse(sprocket)

def update_sprocket(response, id, teeth, pitch_diameter, outside_diameter, pitch):
    sprocket = Sprocket.objects.filter(id=id).update(teeth=teeth, pitch_diameter=pitch_diameter, outside_diameter=outside_diameter, pitch=pitch)
    return HttpResponse('updated')
