import requests

url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"


def get_weather(city: str):
    api_key = '4ee620a05538cbe9bc3f3c6b737bfe2a'
    response = requests.get(url.format(city, api_key))
    data = response.json()
    if data:
        weather_data = {
        'city': data['name'],
        'weather': data['weather'][0]['main'],
        'icon': data['weather'][0]['icon'],
        'temp': data['main']['temp'],
        'humidity': data['main']['humidity'],
    }
    else:
        weather_data: {}

    return weather_data

