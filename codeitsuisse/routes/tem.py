

import logging
import json
from flask import request, jsonify;

from codeitsuisse import app;


logger = logging.getLogger(__name__)


@app.route('/tem', methods=['POST'])
def resdfbdn():
    data = request.get();
    logging.info("data sent for evaluation   {}".format(data))

    #logging.info("My result :{}".format(result))
    return json.dumps(data)
