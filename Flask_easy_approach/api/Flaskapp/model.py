import os
import json
import datetime
import pandas as pd
from prophet.serialize import model_from_json

def forecast(days = 7):
    #model_file = "api/Flaskapp/models/prophet_serialized_model.json"
    model_file = "Flaskapp/models/prophet_serialized_model.json"

    if not os.path.exists(model_file):
        print("Model file could not be found")
        return False

    with open(model_file, 'r') as fin:
        model = model_from_json(json.load(fin))

    #generate future dates

    dates = pd.date_range(start=datetime.datetime.now().date(), end=datetime.datetime.now().date() + datetime.timedelta(days=days), freq='D')
    future = pd.DataFrame({"ds": dates})
    forecast = model.predict(future)
    return forecast[['ds', 'yhat']].tail(days).to_dict("records")

def forecast_one_day():
    print("Accessed forecast_one_day")
    #model_file = "api/Flaskapp/models/prophet_serialized_model.json"
    model_file = "Flaskapp/models/prophet_serialized_model.json"

    if not os.path.exists(model_file):
        print("Model file could not be found from forecast_one_day()")
        return False
    
    with open(model_file, 'r') as fin:
        model = model_from_json(json.load(fin)) 

    dates = pd.date_range(start=datetime.datetime.now().date(), end=datetime.datetime.now().date() + datetime.timedelta(days=1), freq='D')
    future = pd.DataFrame({"ds": dates})  
    forecast = model.predict(future)
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(1).to_dict("records")