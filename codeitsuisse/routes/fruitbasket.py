import logging
import json
import random

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

prv = None

@app.route('/fruitbasket', methods=['POST'])
def fruitbasket():
    data = request.get_json() 
    logging.info("data from request {}".format(data))
    # logging.info("data sent for evaluation {}".format(data))
    random.seed() 
    # logging.info("My result :{}".format(result))
    ans = 0
    guesses = []
    if data:
        for key, value in data.items():
            guess = random.randint(1,100)
            ans += value * guess 
            guesses.append((value, guess))
    print(ans)
    logging.info("current guess: {}".format(guesses))
    return str(ans) 



