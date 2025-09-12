import os
import json
import boto3

def handler(event, context):

    return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": "Hello World"
            
            }
