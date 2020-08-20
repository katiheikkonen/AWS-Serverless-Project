import boto3
import json

eventbridge = boto3.client('events')

def create_eventbridge(event, context):
    payload = json.loads(event['body'])
    user_id = payload['id']
    schedule = payload['schedule']
    rulename = f'ScheduledStepFunction{user_id}'

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

    return {
        "statusCode": 200,
        "body": json.dumps(payload)
    }