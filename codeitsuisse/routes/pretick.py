import logging
import json
import io
import pandas as pd

from pyramid.arima import auto_arima
from collections import deque
from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)




@app.route('/pre-tick', methods=['POST'])
def pre_tick():
    data = request.get_data().decode('utf-8') 
    logging.info("data: {}".format(data))
    data = data.split('\n')[1:]
    logging.info("data {}".format(data))
    data = [i.split(',')[3] for i in data]
    df = pd.DataFrame(data,index=[i for i in range(len(data))], columns=['Close'])
    logging.info("data: {}".format(data))
    print(df)
    # df = pd.read_csv(data_str, sep=",")
    print(df)
    # logging.info("df: {}".format(df))
    # logging.info("data from request {}".format(data))
    # logging.info("data sent for evaluation {}".format(data))
    data = df.sort_index(ascending=True, axis=0)

    n = len(data)
    train = data[:n]
    # val = data[0.7 * n:]
    training = train['Close']
    # validation = val['Close']

    model = auto_arima(training)
    model.fit(training)

    forecast = model.predict(n_periods=1)
    # forecast = pd.DataFrame(forecast,index = valid.index,columns=['Prediction'])    
    print(forecast)



    return str(forecast[0]) 