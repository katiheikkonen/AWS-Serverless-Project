import boto3
import json
import uuid

dynamodb = boto3.resource('dynamodb')

def create_item(event, context):
    json_data = json.loads(event['body'])
    table = dynamodb.Table('userdata')
    uniqueid = uuid.uuid4()

    item = {
        'id': str(uniqueid),
        'username': json_data['username'],
        'email': json_data['email'],
        'city': json_data['city'],
        'country': json_data['country'],
        'notifications': 'N'
    }
    table.put_item(Item=item)

    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response