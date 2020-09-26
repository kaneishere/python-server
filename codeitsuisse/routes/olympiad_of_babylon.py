import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

def solve(data):
    bk,dy=data['books'],data['days']
    bk.sort()
    dy.sort()
    nb,nd=len(bk),len(dy)
    ans=0
    for i in range(nb):
        tmp=bk[:i+1]
        for j in range(nd):
            d=dy[j]
            dp=[0 for i in range(d+1)]
            dp[0]=1
            ind=[[] for i in range(d+1)]
            for k in range(len(tmp)):
                for tot in range(d,tmp[k]-1,-1):
                    if dp[tot]==0 and dp[tot-tmp[k]]:
                        dp[tot]=1
                        ind[tot]=[c for c in ind[tot-tmp[k]]]
                        ind[tot].append(k)
            for k in range(d,0,-1):
                if dp[k]:
                    for c in ind[k][::-1]:
                        tmp.pop(c)
                    break
        if not tmp:
            ans=i+1
        else:
            return ans  
    return nb

@app.route('/olympiad-of-babylon', methods=['POST'])
def olympiad_of_babylon():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    result = solve(data)
    result={'optimalNumberOfBooks':result}
    logging.info("My result :{}".format(result))
    return json.dumps(result);
'''

data={
    "numberOfBooks": 5,
    "numberOfDays": 3,
    "books": [114, 111, 41, 62, 64],
    "days": [157, 136, 130]
}
print(solve(data))
'''




