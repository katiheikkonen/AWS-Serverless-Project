import boto3
import json

def retrieve_user(event, context):
    itemid = event['id']

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('userdata')
    response = table.get_item(
        Key={
            'id': itemid
        })

    return {
        "statusCode": 200,
        'body': json.dumps(response)
    }