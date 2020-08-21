import boto3
import json
import requests

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1')
lambda_client = boto3.client('lambda', region_name='ap-northeast-1')

# function which checks from the database if user already has notifications enabled and acts accordingly
def check_for_notifications(event, context):
    jsondata = json.loads(event['body'])
    userid = jsondata['id']
    table = dynamodb.Table('userdata')
    userinfo = table.get_item(
        Key={
            'id': userid
        })
    # setting up payload for PUT request in case notifications are not yet enabled
    request_payload = {
        "id": userid,
        "username": userinfo['Item']['username'],
        "city": userinfo['Item']['city'],
        "email": userinfo['Item']['email'],
        "country": userinfo['Item']['country'],
        "notifications": "Y"}

    # if notifications are not enabled, send this put request
    if userinfo['Item']['notifications'] == 'N':
        requests.put(f'https://wbm87a0dn0.execute-api.ap-northeast-1.amazonaws.com/Stage/user/{userid}',
                     data=json.dumps(request_payload))

        response = {
            "statusCode": 200,
            "body": json.dumps(jsondata),
            "headers": {"newNotification": "true"}
        }
        # after the notification flag has been updated into the database, another lambda function is invoked with the
        # user id and desired schedule for the notification included in the payload
        lambda_client.invoke(
            FunctionName="arn:aws:lambda:ap-northeast-1:821383200340:function:AWS-Serverless-stack-CreateEventBridge-1AWDV1E9DI3T5",
            InvocationType='Event',
            Payload=json.dumps(response))

    # in case notifications are already enabled, the function only returns a header value which can be processed
    # by the frontend
    else:
        response = {
            "statusCode": 200,
            "body": json.dumps(jsondata),
            "headers": {"newNotification": "false"}
        }

    return response