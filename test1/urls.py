from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('test1', views.TestView)
router.register('city', views.CityView)
router.register('vehicle', views.VehicleView)


urlpatterns = [
    path('', include(router.urls))
]
