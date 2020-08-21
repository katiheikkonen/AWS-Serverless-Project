import requests
import json

def get_covid_data(event, context):

    usercountry = event['Item']['country']
    covid_data = requests.get('https://api.covid19api.com/summary')

    countries_data = covid_data.json()['Countries']

    # filters the object from the entire array of countries where the country is the same as the country in user record
    selected_country = list(filter(lambda countrylist: countrylist['Country'] == usercountry, countries_data))

    # parses out specific data fields from the individual country data
    response = {
        "id": event['Item']['id'],
        "country": selected_country[0]['Country'],
        "new_cases": selected_country[0]['NewConfirmed'],
        "total_cases": selected_country[0]['TotalConfirmed'],
        "new_recovered": selected_country[0]['NewRecovered'],
        "total_recovered": selected_country[0]['TotalRecovered']
    }

    return response

