import boto3
import json

eventbridge = boto3.client('events')

def create_eventbridge():

    #user_id = json.loads(event['body']['id'])
    #schedule = json.loads(event['body']['schedule'])
    #rulename = f'ScheduledStepFunction{user_id}'
    rulename = 'boto3test'

    eventbridge.put_rule(
        Name=rulename,
        ScheduleExpression='cron(0 11 * * ? *)',
        Description='User cron notification rule',
        RoleArn='arn:aws:iam::821383200340:role/AWS-Serverless-KatiMitja'
    )

    eventbridge.put_targets(
            Rule=rulename,
            Targets=[
                {
                    'Arn': 'arn:aws:states:ap-northeast-1:821383200340:stateMachine:Waitstate',
                    'Input':
                        '{"id": "2"}',
                    'Id': 'aws-serverlessproject',
                    'RoleArn': 'arn:aws:iam::821383200340:role/AWS-Serverless-KatiMitja'
                }]
            )

create_eventbridge()