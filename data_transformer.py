
import json
import boto3
import yfinance as yf 

def lambda_handler(event, context):
    tickers = ['FB', 'SHOP', 'BYND', 'NFLX', 'PINS', 'SQ', 'TTD', 'OKTA', 'SNAP', 'DDOG']
    start = '2021-05-11'
    end = '2021-05-12'
    interval = '5m'
    kinesis = boto3.client('kinesis', "us-east-2")
    for ticker in tickers:
        data = yf.download(ticker, start=start, end=end, interval = interval , period = "1d")
        for index, rows in data.iterrows():
            output = json.dumps({
                "high": rows.High, 
                "low": rows.Low, 
                "ts": str(index), 
                "name": ticker
                }) 
            kinesis.put_record(StreamName="STA9760F2020_stream1", Data = output,
             PartitionKey="partitionkey")
                
    return {
        'statusCode': 200,
        'body': json.dumps(output)
    }

