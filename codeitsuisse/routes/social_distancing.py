import logging
import json
import math
from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)



def findsocialdistance(seats, people, spaces):
    def nCr(n,r):
        f = math.factorial
        return f(n) // f(r) // f(n-r)


    if((seats - people)//spaces < (people-1)):
        return (0)


    return(nCr(seats - people + 2 - (people-1)*(spaces-1)-1, people))

@app.route('/social_distancing', methods=['POST'])
def evaluate_social_distancing():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))

    inputValue = data.get("tests")
    ans = {}

    for k, v in inputValue.items():
        ans[k] = findsocialdistance( v.get("seats"), v.get("people"), v.get("spaces"))


    returnvalue = {"answers": ans}
    return jsonify(returnvalue);



