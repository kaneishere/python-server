import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

def solve(tests):
    ans={}
    for t,x in tests.items():
        x=x['floor']
        res=0
        s=sum(x)
        for i in range(1,len(x)):
            if s==0:
                break
            res+=1
            if x[1]==0:
                x[1]+=1
                s+=1
            else:
                x[1]-=1
                s-=1
            if x[i-1]!=0:
                s-=x[i-1]
                res+=2*x[i-1]-1
                if (x[i]<x[i-1]-1):
                    tmp=x[i-1]-1-x[i]
                    if (tmp%2==0):
                        s-=x[i]
                        x[i]=0
                    else:
                        s-=x[i]-1
                        x[i]=1
                else:
                    tmp=x[i]-x[i-1]+1
                    s-=tmp
                    x[i]-=tmp
                if s==0:
                    break
        if s!=0:
            tmp=x[len(x)-1]
            res+=2*tmp
            if (tmp%2==1):
                res+=1
        ans[t]=res
    return ans

@app.route('/clean_floor', methods=['POST'])
def clean_floor():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    result=solve(data['tests'])
    result={"answers":result}
    logging.info("My result :{}".format(result))
    return json.dumps(result)



