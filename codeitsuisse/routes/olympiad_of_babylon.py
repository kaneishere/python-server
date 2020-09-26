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
        dd=dy[:]
        mi,cur,pp=1000000000,0,[]
        for x in range(nd):
            for j in range(len(dd)):
                d=dd[j]
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
                        if d-k<=mi:
                            mi=d-k
                            cur=d
                            pp=[y for y in ind[k][::-1]]
                        break
            for x in pp:
                tmp.pop(x)
            dd.remove(cur)
            mi=1000000000
            if not tmp:
                break;
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
data={'numberOfDays': 10, 'numberOfBooks': 50, 'books': [70, 57, 40, 35, 27, 29, 61, 53, 54, 71, 28, 49, 72, 64, 44, 56, 47, 66, 29, 32, 42, 51, 53, 43, 69, 48, 68, 73, 28, 55, 77, 63, 60, 35, 33, 51, 67, 79, 31, 29, 37, 31, 65, 50, 39, 75, 62, 35, 80, 26], 'days': [105, 86, 118, 99, 85, 108, 109, 116, 92, 119]}
print(solve(data))
data={'numberOfDays': 5, 'numberOfBooks': 16, 'books': [71, 79, 57, 36, 36, 63, 67, 69, 52, 31, 61, 37, 42, 48, 69, 52], 'days': [118, 85, 105, 116, 92]}
'''



