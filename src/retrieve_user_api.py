import boto3
import json

dynamodb = boto3.resource('dynamodb')

def retrieve_user_api(event, context):
    itemid = event['pathParameters']['id']

    table = dynamodb.Table('checkpoint7')
    response = table.get_item(
        Key={
            'id': itemid
        })

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }