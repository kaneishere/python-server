import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

memo = list()
def solve(ar, memo, i = 0):
    if sum(ar) == 0:
        return 0
    total = 0 if i == 0 else sum(ar[:i]) 

    if total in memo[i]: 
        return memo[i][total]

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
        left = solve(ar, memo, i-1) + 1
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
        right = solve(ar, memo, i+1) + 1
        if add:
            ar[i+1] -= 1
        else:
            ar[i-1] += 1

    memo[i][total] = min(left,right)
    return memo[i][total]



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
        memo = [{} for i in range(n)]
        ans = solve(ar, memo)
        results["answers"][key] = ans

    return json.dumps(results);



