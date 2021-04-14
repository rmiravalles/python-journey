# A weather program
import requests

api_key = '2d86b24dfd297cd013b33828cca71265'
city = 'Madrid'
url = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+api_key+''

request = requests.get(url)

json = request.json()
print()
