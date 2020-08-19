import boto3

def retrieve_user(event, context):
    itemid = event['id']

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('userdata')
    response = table.get_item(
        Key={
            'id': itemid
        })

    return response