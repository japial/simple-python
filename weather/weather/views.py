from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from weather import weather_service


def index(request: HttpRequest):
    cities = ['Dhaka', 'Chittagong', 'Rangpur', 'Sylhet', 'Khulna', 'Rajshahi']
    weather_data = [weather_service.get_weather(city) for city in cities]
    return render(request, 'index.html', context={'weather_data': weather_data})
