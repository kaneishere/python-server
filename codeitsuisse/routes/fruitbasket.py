import logging
import json
import random

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)



@app.route('/fruitbasket', methods=['POST'])
def fruitbasket():
    data = request.get_json();
    logging.info("data from request {}".format(data))
    # logging.info("data sent for evaluation {}".format(data))
    random.seed(random.randint()) 
    # logging.info("My result :{}".format(result))
    ans = 0
    if data:
        for key, value in data.items():
            ans += value * random.randint(1,100)
    print(ans)

    return str(ans) 



