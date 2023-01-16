from dataclasses import field
from rest_framework import serializers
from .models import test1, city, vehicle


class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = test1
        exclude = ()
        field = ('id', 'name', 'city')
        # fields = '__all__'


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = city
        exclude = ()
        field = ('id', 'name')
        # fields = '__all__'


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = vehicle
        exclude = ()
        field = ('id', 'name', 'test1')
        # fields = '__all__'
