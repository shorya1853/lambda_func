import json
import boto3
import os

profile = os.getenv("PROFILE_NAME")

session = boto3.Session(profile_name=profile)

sqs = session.client("sqs", region_name='ap-south-1')
sqs_queue_url = "https://sqs.ap-south-1.amazonaws.com/893711537471/url_queue"

def lambda_handler(event, context):
    # TODO implement
    key = event['Records'][0]['s3']['object']['key']
    message_body = key
    # response = sqs.receive_message(
    #     QueueUrl=sqs_queue_url,
    #     AttributeNames=[
    #         'SentTimestamp'
    #     ],
    #     MaxNumberOfMessages=1,
    #     MessageAttributeNames=[
    #         'All'
    #     ],
    #     VisibilityTimeout=0,
    #     WaitTimeSeconds=0
    # )
    
    response = sqs.send_message(
    QueueUrl=sqs_queue_url,
    MessageBody=message_body
    )
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
