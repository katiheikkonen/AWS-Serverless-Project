import boto3


dynamodb = boto3.resource("dynamodb")

def delete_user(event, context):
    itemid = event['pathParameters']['id']
    table = dynamodb.Table('userdata')

    table.delete_item(Key={
        'id': itemid
    })
    print(event)
    return {
        'statusCode': 200
    }