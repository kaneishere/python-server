import logging
import json
import random

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

last_guess = {}
last_sum = 0

w = {'maPomegranate': 59,
 'maPineapple': 7,
 'maAvocado': 32,
 'maRambutan': 42,
 'maApple': 31,
 'maWatermelon': 84} 
@app.route('/fruitbasket', methods=['POST'])
def fruitbasket():
    data = request.get_data() 
    data = json.loads(data.decode('utf-8'))
    logging.info("data from request {}".format(data))
    # logging.info("data sent for evaluation {}".format(data))
    # random.seed() 
    # logging.info("My result :{}".format(result))
    ans = 0
    for key,value in data.items():
         ans +=  w[key] * value

    
    # print(ans)
    # logging.info("current guess: {}".format(guesses))
    # last_sum = ans
    return str(ans)



