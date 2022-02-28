import json
import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    response = dynamodb.scan(TableName="Lambda-Operations",
        FilterExpression="orderId = :id and quantity > :q",
        ExpressionAttributeValues={
            ':id': {'S': event['orderId']},
            ':q': {'N': event['quantity']}
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(response["Items"])
    }
