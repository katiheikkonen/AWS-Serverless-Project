import boto3
import requests
import json

ssm = boto3.client('ssm', region_name='ap-northeast-1')


def get_weather_data(event, context):
    parameter = ssm.get_parameter(Name='WeatherAPI', WithDecryption=True)
    apikey = parameter['Parameter']['Value']

    usercity = event['Item']['city']
    weather_data = requests.get(
        f'https://api.openweathermap.org/data/2.5/forecast?units=metric&q={usercity}&appid={apikey}')
    city_data = weather_data.json()
    data = {
        "weather": city_data['list'][0]['weather'][0]['main'],  # weather (Clear, Clouds, Rain)
        "weather_decription": city_data['list'][0]['weather'][0]['description'],  # more precise description on weather
        "temperature": city_data['list'][0]['main']['temp'],  # current temperature
        "feels_like": city_data['list'][0]['main']['feels_like']  # what temperature feels like
    }

    return data


