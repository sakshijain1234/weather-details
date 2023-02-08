import requests
import os
from datetime import datetime

user_api= os.environ['current_weather_data']
location= input("Enter the city name:")

complete_api_link= "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

api_link= requests.get(complete_api_link)
api_data= api_link.json()
#print(api_data)

if api_data['cod'] == '404':
    print("Invalid City: {}, Please check you city name".format(location))
else:
    temp_city= ((api_data['main']['temp'])-273.15)
    weather_desc= api_data['weather'][0]['description']
    hmdt= api_data['main']['humidity']
    wind_spd= api_data['wind']['speed']
    min_temp=((api_data['main']['temp_min'])-273.15)
    max_temp=((api_data['main']['temp_max'])-273.15)
    date_time= datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print("-----------------------------------------------------------")
    print("Weather stats for - {} || {}".format(location.upper(), date_time))
    print("-----------------------------------------------------------")

    print("curret temperature is: {:.2f} deg C".format(temp_city))
    print("current weather desc :",weather_desc)
    print("current humidity :",hmdt, '%')
    print("current wind speed :",wind_spd,'kmph')
    print("minimum temperature : {:.2f} degree C",min_temp)
    print("maximum temperature : {:.2f} degree C",max_temp)
    
