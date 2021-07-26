from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Car
import json



def car_view(request):
    if request.method not in ["GET", "POST"]:
        return HttpResponse(status=405)

    if request.method == "GET":
        cars = Car.objects.all()
        data = [{"id": car.id, "name": car.name} for car in cars]
        return JsonResponse(data, safe=False, status=200)

    if request.method == "POST":
        data = json.loads(request.body)
        car = Car.objects.create(**data)
        context = {"id": car.id, "name": car.name}

        return JsonResponse(context, status=201)
