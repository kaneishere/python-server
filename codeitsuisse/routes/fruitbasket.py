import logging
import json
import random

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

prv = None

@app.route('/fruitbasket', methods=['POST'])
def fruitbasket():
    data = request.get_data() 
    data = json.loads(data.decode('utf-8'))
    logging.info("data from request {}".format(data))
    # logging.info("data sent for evaluation {}".format(data))
    random.seed() 
    # logging.info("My result :{}".format(result))
    ans = 0
    values = list(data.values())
    guesses = [80, 90, 50]

    if data:
        for value, guess in zip(values, guesses): 
            
            ans += value * guess 
            guesses.append((value, guess))
    
    print(ans)
    logging.info("current guess: {}".format(guesses))
    return str(ans) 



