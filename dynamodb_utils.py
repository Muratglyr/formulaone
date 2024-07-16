import boto3
import pandas as pd
import json

def load_config(config_path='config.json'):
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config

def load_data_from_dynamodb():
    config = load_config()
    dynamodb = boto3.resource(
        'dynamodb',
        aws_access_key_id=config['aws_access_key_id'],
        aws_secret_access_key=config['aws_secret_access_key'],
        region_name=config['region_name']
    )
    table = dynamodb.Table(config['table_name'])
    response = table.scan()
    data = response['Items']
    df = pd.DataFrame(data)
    return df
