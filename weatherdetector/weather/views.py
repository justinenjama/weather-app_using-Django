from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        APIKEY = '' # use your API key
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+APIKEY).read() # sending reguest to weather map
        json_data = json.loads(res) # receiving the data from weather map as a json file
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' +
            str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp'])+'K',
            "pressure": str(json_data['main']['pressure']) + 'Pa',
            "humidity": str(json_data['main']['humidity']) + '%',
            "wind": str(json_data['wind']['speed']) + 'km/h',
            "sea_level": str(json_data['main']['sea_level']) + 'Pa',
            "visibility": str(json_data['visibility']) + 'm',
            "cloudiness": str(json_data['clouds']['all']) + '%',
            "weather_description": json_data['weather'][0]['description'],
            "weather_icon": json_data['weather'][0].get('icon'),
        }     
    else:
        city = ''
        data = {}  # returning an empty dictionary
    return render(request, 'index.html', {'city': city, 'data': data}) 
