from alpha_vantage.timeseries import TimeSeries
from pymongo import MongoClient
import json


def get_difference_day(value_days):
    value_difference = -1
    values = []
    for value in value_days:
        if(value_difference == -1):
            values.append(value)
        else:
            values.append(value - value_difference)
        value_difference = value
    return values

def get_porcentage_difference(value_days):
    value_difference = -1
    values = []
    for value in value_days:
        if(value_difference == -1):
            values.append((1.0 - value/value) * 100)
        else:
            values.append((value/value_difference - 1.00) * 100)
        value_difference = value
    return values


with open("creds/alpha.json") as f:
    creds = json.loads(f.read())

api = creds["api"]

ts = TimeSeries(key=api, output_format='json')

data, meta_data = ts.get_daily('BIDI4.SA')

for i in data:
    stock = {
        "date": i,
        "value": data[i]["4. close"],
        "stock": "BIDI4" 
    }
    print(stock)

