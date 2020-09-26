import logging
import json
import functools

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

def solve(data):
    ans=[]
    for t in data:
        v,spot=t['Portfolio']['Value'],t['Portfolio']['SpotPrcVol']
        a=t['IndexFutures']
        rat,fpr,nof=float('inf'),float('inf'),float('inf')
        for ind,i in enumerate(a):
            i['OptimalHedgeRatio']=round(i["CoRelationCoefficient"]*spot/i["FuturePrcVol"],3)
            i["NumFuturesContract"]=i['OptimalHedgeRatio']*v/(i["IndexFuturePrice"]*i["Notional"])

            if i['OptimalHedgeRatio']<rat and i['FuturePrcVol']<fpr:
                cur=ind
            elif i['OptimalHedgeRatio']>=rat and i['FuturePrcVol']>=fpr:
                continue
            elif (i['NumFuturesContract']<nof):
                cur=ind
            rat,fpr,nof=a[cur]['OptimalHedgeRatio'],a[cur]['FuturePrcVol'],a[cur]['NumFuturesContract']

        ans.append({"HedgePositionName":a[cur]["Name"],"OptimalHedgeRatio":a[cur]["OptimalHedgeRatio"],"NumFuturesContract":int(a[cur]["NumFuturesContract"]+0.5)})
    return ans

@app.route('/optimizedportfolio', methods=['POST'])
def optimizedportfolio():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("input");
    result = solve(data['inputs'])
    result = {"outputs":result}
    logging.info("My result :{}".format(result))
    return json.dumps(result);



