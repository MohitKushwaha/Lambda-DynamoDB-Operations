import json
import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    response = dynamodb.query(TableName="Lambda-Operations",
        KeyConditionExpression="orderId = :id",
        ExpressionAttributeValues={
            ':id': {'S': event['orderId']}
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(response["Items"])
    }
