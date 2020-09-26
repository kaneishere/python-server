import logging
import json
import random

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/contact_trace', methods=['POST'])
def fruitbasket():
    data = request.get_data() 
    data = json.loads(data.decode('utf-8'))
    logging.info("data from request {}".format(data))
    # logging.info("data sent for evaluation {}".format(data))
    # random.seed() 
    # logging.info("My result :{}".format(result))
    infected = data["infected"]
    origin = data["origin"]
    cluster = data["cluster"]
    # m -> name, genome
    m = { key : value for key, value in cluster.items() }
    m[origin['name']] = origin['genome']
    open_dict = { infected }
    explored = []
    ans = []

    dfs()



