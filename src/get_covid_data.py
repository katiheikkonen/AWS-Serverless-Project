import requests
import json

def get_covid_data(event, context):

    usercountry = event['Item']['country']
    covid_data = requests.get('https://api.covid19api.com/summary')

    countries_data = covid_data.json()['Countries']
    response = list(filter(lambda countrylist: countrylist['Country'] == usercountry, countries_data))

    return response[0]
