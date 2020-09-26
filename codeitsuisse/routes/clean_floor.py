import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

def solve(ar, i = 0):
    if sum(ar) == 0:
        return 0
    
    mx = 1000000000000000
    left = mx
    right = mx
    if i > 0:
        add = False
        if ar[i-1] == 0:
            ar[i-1] += 1
            add = True
        else:
            ar[i-1] -= 1
        left = solve(ar, i-1) + 1
        if add:
            ar[i-1] -= 1
        else:
            ar[i-1] += 1
    
    if i < len(ar) - 1:
        add = False
        
        if ar[i+1] == 0:
            ar[i+1] += 1
            add = True
        else:
            ar[i+1] -= 1
        right = solve(ar, i+1) + 1
        if add:
            ar[i+1] -= 1
        else:
            ar[i-1] += 1

    return min(left,right)



@app.route('/clean_floor', methods=['POST'])
def clean_floor():
    data = request.get_json();
    logging.info("data from request {}".format(data))
    # logging.info("data sent for evaluation {}".format(data))
    tests = data["tests"]
    # logging.info("My result :{}".format(result))
    n = len(tests)
    results = { "answers" : {}}
    keys = list(tests.keys())
    for key in keys:
        ar = tests[key]["floor"]
        print(ar)
        ans = solve(ar)
        results["answers"][key] = ans

    return json.dumps(results);



