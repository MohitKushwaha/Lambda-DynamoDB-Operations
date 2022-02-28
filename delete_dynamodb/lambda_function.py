import json
import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    record = dynamodb.delete_item(TableName="Lambda-Operations",
        Key={
            "orderId": {'S': event['orderId']},
            "userEmail": {'S': event['userEmail']}
        },
        ConditionExpression="quantity < :q",
        ExpressionAttributeValues= {
            ':q': {'N': "1"}
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(record)
    }
