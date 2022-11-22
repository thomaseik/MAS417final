# Using this youtube tutorial: https://www.youtube.com/watch?v=9P5MY_2i7K8  to get temperature at requested location

import requests
import Main

#Sets up the API request
base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = "d8689764d384f4e0d91249bf557f48d0"
city = Main.city

url = base_url + "appid=" + api_key + "&q=" + city

response = requests.get(url).json()


def kelvin_to_celsius(kelvin):
    celsius = round(kelvin - 273.15, 2)
    return celsius

#Retrieve temperature in kelvin from response
temp_kelvin = response['main']['temp']
temp_celsius = kelvin_to_celsius(temp_kelvin)
print(temp_celsius)
