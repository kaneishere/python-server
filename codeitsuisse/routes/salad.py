import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/salad-spree', methods=['POST'])
def salad():
    data = request.get_json();
    n = data["number_of_salads"]
    salads = data["salad_prices_street_map"]
    # print(data)
    # logging.info("data sent for evaluation {}".format(data))
    mx = 100000000000000000000000 
    cost = mx
    for street in salads:
        i = 0
        m = len(street) 
        while i + n - 1 < m:
            cur_cost = 0
            for j in range(i, i + n):
                if street[j] == "X":
                    cur_cost = mx
                    break
                cur_cost += int(street[j])
            
            cost = min(cost, cur_cost)
            i += 1
    ans = {}
    if cost == mx:
        ans["result"] = 0
    else:
        ans["result"] = cost

    # logging.info("My result :{}".format(data))
    return json.dumps(ans);



