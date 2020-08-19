import boto3
import json
client = boto3.client('sns')

def sns(event, context):

    client.publish(
        TopicArn='arn:aws:sns:us-east-1:821383200340:Travel-info',
        Message='',
        Subject='Your Daily Travel Info'
    )
    response = {
        "statusCode": 200,
        "body": "Message sent"
    }
    return response
