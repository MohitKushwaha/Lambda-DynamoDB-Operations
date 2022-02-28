import json
import boto3
from datetime import datetime

dynamodb = boto3.client('dynamodb')
    
def lambda_handler(event, context):
 #if 'quantity' doesn't isn't sent from client side, set the default value of 1
 if not 'quantity' in event:
  event['quantity'] = 1
  
 record = dynamodb.put_item(TableName='Lambda-Operations', Item={
      "orderId": {
       "S": event['orderId']
      },
      "userEmail": {
       "S": event['userEmail']
      },
      "productId": {
       "S": event['productId']
      },
      "status": {
       "S": event['status']
      },
      "quantity": {
       "N": event['quantity']
      },
      "datetime": {
       "S": datetime.now().strftime("%d %b %Y, %H:%M:%S")
      }
 })
 
 return {
     'statusCode': 200,
     'body': json.dumps(record)
 }
