import requests

API_KEY = "54331c3986c51e8d7b6803d31661f6cb"
BASE_URL ="http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print("Weather: ",weather)
    temperature = data ["main"]["temp"] - 273.15
    
    
    print("Temperature:",temperature, "celsius")
else:
    print("An error occured.")


