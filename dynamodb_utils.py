import boto3
import pandas as pd

def load_data_from_dynamodb(table_name, region_name='us-west-2'):
    dynamodb = boto3.resource('dynamodb', region_name=region_name)
    table = dynamodb.Table(table_name)
    response = table.scan()
    data = response['Items']
    df = pd.DataFrame(data)
    return df
