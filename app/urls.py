from django.contrib import admin
from django.urls import path, include
from .views import CitiesWeather, WeatherByCity

urlpatterns = [
    path('api1/', CitiesWeather.as_view()),
    path('api1/', WeatherByCity.as_view()),
]