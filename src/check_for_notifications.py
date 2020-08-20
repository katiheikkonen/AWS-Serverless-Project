import boto3
import json
import requests

dynamodb = boto3.resource('dynamodb')


def check_for_notifications(event, context):
    jsondata = json.loads(event['body'])
    userid = jsondata['id']
    table = dynamodb.Table('userdata')
    userinfo = table.get_item(
        Key={
            'id': userid
        })

    request_payload = {
        "id": userid,
        "username": userinfo['Item']['username'],
        "city": userinfo['Item']['city'],
        "email": userinfo['Item']['email'],
        "country": userinfo['Item']['country'],
        "notifications": "Y"}

    if userinfo['Item']['notifications'] == 'N':
        requests.put(f'https://tww2nnv9fk.execute-api.ap-northeast-1.amazonaws.com/Stage/user/{userid}',
                     data=json.dumps(request_payload))

        response = {
            "statusCode": 200,
            "body": event['body'],
            "headers": {"newNotification": "true"}
        }

    else:
        response = {
            "statusCode": 200,
            "body": event['body'],
            "headers": {"newNotification": "false"}
        }

    return response
