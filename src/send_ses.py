import boto3
import json

client = boto3.client('ses')

def send_ses(event, context):
    name = event[0]['username']
    email = event[0]['email']
    city = event[0]['city']
    country = event[1]['country']
    weather = event[0]['weather']
    weather_description = event[0]['weather_description']
    temperature = event[0]['temperature']
    feels_like = event[0]['feels_like']
    new_cases = event[1]["new_cases"]
    total_cases = event[1]["total_cases"]
    new_recovered = event[1]["new_recovered"]
    total_recovered = event[1]["total_recovered"]

    if weather == "Clouds":
        if weather_description != "overcast clouds":
            weather_message = f"Weather is going to be {weather_description}."
        else:
            weather_message = "Weather is going to be cloudy."
    elif weather == "Clear":
        weather_message = "Weather is going to be sunny so remember your sunglasses!"
    elif weather == "Rain":
        weather_message = "It's going to rain so remember to bring your umbrella!"
    else:
        weather_message = ""

    message = f'Hello {name}!\nThis is your daily report from Fantastic Travels.\
    \nIt is currently {temperature} °C in {city} and it feels like {feels_like} °C.\
    \n{weather_message}\nYour daily Covid-19 statistics:\
    \nThere are {new_cases} new Covid-19 cases in {country}. The total number of cases in {country} is {total_cases}.\
    \nThere are {new_recovered} new recoveries in {country} today and the total number of recoveries is {total_recovered}.\
    \nStay safe and wash your hands!'

    client.send_email(
        Source='tsttestitesti@gmail.com',
        Destination={
            'ToAddresses': [
                email,
            ],
        },
        Message={
            'Subject': {
                'Data': 'Your Daily Travel Info'
            },
            'Body': {
                'Text': {
                    'Data': message
                }
            }
        }
    )
    response = {
        "statusCode": 200,
        "body": json.dumps("Message sent")
    }
    return response