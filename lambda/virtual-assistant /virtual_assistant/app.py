import json
import boto3
import os
# import requests


def lambda_handler(event, context):
    # Load environmental variables
    env_region = os.environ['REGION']
    email_text = os.environ['VAR1']

    comprehend_results = invoke_comprehend(email_text, env_region)


    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }


def invoke_comprehend(input_text, env_region):
    # get the region of comprehend service   
    comprehend_client = boto3.client(service_name='comprehend', region_name=env_region)

    return "success"