import boto3
import json

dynamodb = boto3.resource('dynamodb')

def update_item(event, context):
    table = dynamodb.Table('userdata')
    data = json.loads(event['body'])
    result = table.update_item(
        Key={
            'id': event['pathParameters']['id']
        },
        ExpressionAttributeValues={
            ':city': data['city'],
            ':country': data['country'],
            ':email': data['email'],
            ':username': data['username'],
            ':notifications': data['notifications']
        },
        UpdateExpression='SET city = :city, country = :country, email = :email, username = :username, notifications = :notifications',
        ReturnValues='ALL_NEW'
    )
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'])
    }
    return response