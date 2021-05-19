# Streaming-Finance-Data-with-AWS-Lambda
This project includes the process of consuming “real time” data, processing the data and then dumping it in a manner that facilitates querying and further analysis, either in real time or near 
real time capacity
### Infrastructure 
This project consists of three major infrastructure elements that work in tandem:
1.	A lambda function that gathers our data (**DataTransformer**)
2.	A Kinesis stream that holds our data (**DataCollector**)
3.	A serverless process that allows us to query our S3 data (**DataAnalyzer**)

### Data Transformation
In our collector lambda, using the yfinance module (documentation here) to grab pricing information for each of the following stocks: <br />
●	Beyond Meat (BYND) <br />
●	Datadog (DDOG) <br />
●	Facebook (FB) <br />
●	Netflix (NFLX) <br />
●	Okta (OKTA) <br />
●	Pinterest (PINS)<br />
●	Shopify (SHOP)  <br />
●	Snap (SNAP) <br />
●	Square (SQ) <br />
●	The Trade Desk (TTD)
### Lambda Source Code For DataCollector
[Data_transformer](https://github.com/Janetle-hi/Streaming-Finance-Data-with-AWS-Lambda/blob/main/data_transformer.py) <br /><br />
![confi](https://github.com/Janetle-hi/Streaming-Finance-Data-with-AWS-Lambda/blob/main/asset/kinesis_config.png)


