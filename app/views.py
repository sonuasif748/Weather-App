from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import urllib.request
import json

# Create your views here.
APIKey = 'ef5954e904547b2409004ec38ac1074b'

class CitiesWeather(APIView):
    def get(self, request):
        cities = ["Hyderabad","Mumbai","Delhi","Bangalore","Ahmedabad","Chennai","Kolkata","Surat","Pune","Jaipur","Kanpur",
                  "Nagpur","Indore","Thane","Bhopal","Visakhapatnam","Patna","Vadodara","Ghaziabad","Ludhiana","Agra",
                  "Nashik","Faridabad","Rajkot","Varanasi","Srinagar","Amritsar","Allahabad","Thiruvananthapuram","Ranchi"]
        data = []
        for city in cities:
            source = urllib.request.urlopen(
                'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid='+ APIKey).read()
            fulldata = {"coord":{"lon":78.4744,"lat":17.3753},
                        "weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],
                        "base":"stations","main":{"temp":300.38,"feels_like":303.74,"temp_min":300.38,"temp_max":303.88,
                                                  "pressure":1011,"humidity":83},
                        "visibility":6000,"wind":{"speed":5.14,"deg":300},"clouds":{"all":40},"dt":1661580529,
                        "sys":{"type":1,"id":9214,"country":"IN","sunrise":1661560294,"sunset":1661605462},
                        "timezone":19800,"id":1269843,"name":"Hyderabad","cod":200}
            list_of_data = json.loads(source)
            data.append({
                'city': city,
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ' '
                              + str(list_of_data['coord']['lat']),
                "weather":str(list_of_data['weather'][0]['main']),
                "temp": str(list_of_data['main']['temp']) + 'k',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
            })
        return Response(data)


class WeatherByCity(APIView):
    def get(self, request):
        params = request.query_params
        city = params['city']
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid='+ APIKey).read()
        fulldata = {"coord":{"lon":78.4744,"lat":17.3753},
                    "weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],
                    "base":"stations","main":{"temp":300.38,"feels_like":303.74,"temp_min":300.38,"temp_max":303.88,
                                              "pressure":1011,"humidity":83},
                    "visibility":6000,"wind":{"speed":5.14,"deg":300},"clouds":{"all":40},"dt":1661580529,
                    "sys":{"type":1,"id":9214,"country":"IN","sunrise":1661560294,"sunset":1661605462},
                    "timezone":19800,"id":1269843,"name":"Hyderabad","cod":200}
        list_of_data = json.loads(source)
        data = {
            'city': city,
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                          + str(list_of_data['coord']['lat']),
            "weather":str(list_of_data['weather'][0]['main']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        return Response(data)