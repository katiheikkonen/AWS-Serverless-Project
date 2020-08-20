import boto3
import json

eventbridge = boto3.client('events')


def create_eventbridge(event, context):
    jsondata = json.loads(event['body'])
    user_id = jsondata['id']
    schedule = jsondata['schedule']
    rulename = f'ScheduledStepFunction{user_id}'

    headers = event['headers']

    if headers['newNotification'] == "true":

        eventbridge.put_rule(
            Name=rulename,
            ScheduleExpression=f'cron(0 {schedule} * * ? *)',
            Description='User cron notification rule',
            RoleArn='arn:aws:iam::821383200340:role/AWS-Serverless-KatiMitja'
        )

        eventbridge.put_targets(
            Rule=rulename,
            Targets=[
                {
                    'Arn': 'arn:aws:states:ap-northeast-1:821383200340:stateMachine:Waitstate',
                    'Input':
                        json.dumps({"id": user_id}),
                    'Id': 'aws-serverlessproject',
                    'RoleArn': 'arn:aws:iam::821383200340:role/AWS-Serverless-KatiMitja'
                }]
        )

        response = {
            "statusCode": 200,
            "body": json.dumps(jsondata)
        }

    else:

        response = {
            "statusCode": 200,
            "body": json.dumps(jsondata),
            "headers": {"notification": "exists"}
        }

    return response