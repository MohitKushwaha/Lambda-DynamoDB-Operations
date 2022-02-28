import json
import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    record = dynamodb.update_item(TableName='Lambda-Operations', 
        Key= {
            "orderId": {'S': event['orderId']},
            "userEmail": {'S': event['userEmail']}
        },
        UpdateExpression="set #stat=:s",
        ConditionExpression="quantity > :q",
        ExpressionAttributeNames= {
            '#stat': "status"
        },
        ExpressionAttributeValues= {
            ':s': {'S': "premium"},
            ':q': {'N': "5"}
        },
        ReturnValues= "UPDATED_NEW"
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(record)
    }
