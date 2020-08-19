import requests
import json
import os

def get_weather_data(event, context):

    usercity = json.loads(event['Item']['city'])
    my_api_key = os.environ['APIKEY']
    weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?units=metric&q={usercity}&appid={my_api_key}')
    city_data = weather_data.json()
    data = {
        "weather": city_data['list'][0]['weather'][0]['main'], #  weather (Clear, Clouds, Rain)
        "weather_decription": city_data['list'][0]['weather'][0]['description'], #  more precise description on weather
        "temperature": city_data['list'][0]['main']['temp'], #  current temperature
        "feels_like": city_data['list'][0]['main']['feels_like'] # what temperature feels like
    }
    print(json.dumps(data))
    return {
         "statusCode": 200,
         'body': json.dumps(data)
    }

