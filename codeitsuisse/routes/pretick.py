import logging
import json
import io
import pandas as pd
import numpy as np
# from sklearn.preprocessing import MinMaxScaler
# from keras.models import Sequential
# from keras.layers import Dense, Dropout, LSTM

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
    # logging.info("df: {}".format(df))
    # logging.info("data from request {}".format(data))
    # logging.info("data sent for evaluation {}".format(data))
    dataset = df.sort_index(ascending=True, axis=0)
    df['Predict'] = df['Close'].rolling(window=50).mean()
    print(df['Predict'])

    return str(df['Predict'][len(df)-1]) 