import boto3
import json
import requests

dynamodb = boto3.resource('dynamodb')

def check_for_notifications(event, context):

    userid = json.loads(event['body']['id'])
    table = dynamodb.Table('userdata')
    userinfo = table.get_item(
        Key={
            'id': userid
        })

    request_payload = {
        "id": userinfo['id'],
        "username": userinfo['username'],
        "city": userinfo['city'],
        "country": userinfo['country'],
        "notifications": "Y"
    }

    if userinfo['notifications'] == 'N':
        requests.put(f'https://tww2nnv9fk.execute-api.ap-northeast-1.amazonaws.com/Stage/user/{userid}',
                     data=json.dumps(request_payload))

        return {
            "statusCode": 200,
            "body": json.dumps(event),
            "newNotification": 'true'
        }

    else:
        return {
            "statusCode": 200,
            "body": json.dumps(event),
            "newNotification": 'false'
        }
