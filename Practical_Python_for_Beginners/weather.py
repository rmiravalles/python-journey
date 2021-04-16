# A weather program
import requests

def get_weather():
    api_key = '2d86b24dfd297cd013b33828cca71265'
    city = 'Madrid'
    url = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+api_key+'&units=metric'

    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {
        'description': description,
        'temp_min': temp_min,
        'temp_max': temp_max,
        }

def main():
    weather_dict = get_weather()
    print(f"Today's forecast is {weather_dict.get('description')}.")
    print(f"The minimum temperature is {weather_dict.get('temp_min')}.")
    print(f"The maximum temperature is {weather_dict.get('temp_max')}.")

main()

