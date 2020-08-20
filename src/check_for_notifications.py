import boto3
import json
import requests

dynamodb = boto3.resource('dynamodb')
lambda_client = boto3.client('lambda', region_name='ap-northeast-1')


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
        requests.put(f'https://wbm87a0dn0.execute-api.ap-northeast-1.amazonaws.com/Stage/user/{userid}',
                     data=json.dumps(request_payload))

        response = {
            "statusCode": 200,
            "body": json.dumps(jsondata),
            "headers": {"newNotification": "true"}
        }

        lambda_client.invoke(
            FunctionName="arn:aws:lambda:ap-northeast-1:821383200340:function:AWS-Serverless-stack-CreateEventBridge-1AWDV1E9DI3T5",
            InvocationType='Event',
            Payload=json.dumps(response))

    else:
        response = {
            "statusCode": 200,
            "body": json.dumps(jsondata),
            "headers": {"newNotification": "false"}
        }

    return response