''' TODO: CRONTAB FOR DAILY RUNS '''

import json
import boto3
ssm = boto3.client('ssm', 'ca-central-1')


def get_parameters():
    response_parms = {}
    response = ssm.get_parameters(
        Names=['LambdaSecureString'], WithDecryption=True
    )
    for parameter in response['Parameters']:
        response_parms[parameter] = parameter['value']
    return response_parms
        
params = get_parameters()
print(params)