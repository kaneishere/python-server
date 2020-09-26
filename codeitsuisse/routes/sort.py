import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/sort', methods=['POST'])
def sort():
    data = request.get_json();
    # print(data)
    logging.info("data sent for evaluation {}".format(data))
    data.sort() 
    logging.info("My result :{}".format(data))
    return json.dumps(data);



