import boto3
import json

client = boto3.client('sns')
client = boto3.client('ses')

def send_ses(event, context):
    name = event['output'][0]['username']
    city = event['output'][0]['city']
    country = event['output'][1]['country']
    weather = event['output'][0]['weather']
    temperature = event['output'][0]['temperature']
    feels_like = event['output'][0]['feels_like']
    new_cases = event['output'][1]["new_cases"]
    total_cases = event['output'][1]["total_cases"]
    new_recovered = event['output'][1]["new_recovered"]
    total_recovered = event['output'][1]["total_recovered"]

    if weather == "Clouds":
        weather_message = "It's going to be cloudy."
        photo = 'https://aws-bucket-serverless.s3-ap-northeast-1.amazonaws.com/clouds.jpg'
    elif weather == "Clear":
        weather_message = "Weather is going to be sunny so remember your sunglasses!"
        photo = 'https://aws-bucket-serverless.s3-ap-northeast-1.amazonaws.com/sun.jpg'
    elif weather == "Rain":
        weather_message = "It's going to rain so remember to bring your umbrella!"
        photo = 'https://aws-bucket-serverless.s3-ap-northeast-1.amazonaws.com/rain.jpg'
    else:
        weather_message = ""

    message = f'Hello {name}!\nThis is your daily report from Kati and Mitja Fantastic Travels.\n\
    It is currently {temperature} °C in {city} and it feels like {feels_like} °C. \
    \n{weather_message}\nYour daily Covid-19 statistics: \n \
    There are {new_cases} new Covid-19 cases in {country}. The total number of cases in {country} is {total_cases}.\n \
    There are {new_recovered} new recoveries in {country} today and the total number of recoveries is {total_recovered}.'

    client.send_email(
        Source='tsttestitesti@gmail.com',
        Destination={
            'ToAddresses': [
                'tsttestitesti@gmail.com',
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