from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import test1, city, vehicle
from .serializer import TestSerializer, CitySerializer, VehicleSerializer


class TestView(viewsets.ModelViewSet):
    queryset = test1.objects.all()
    serializer_class = TestSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class CityView(viewsets.ModelViewSet):
    queryset = city.objects.all()
    serializer_class = CitySerializer


class VehicleView(viewsets.ModelViewSet):
    queryset = vehicle.objects.all()
    serializer_class = VehicleSerializer
