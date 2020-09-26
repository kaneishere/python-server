import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

def solve(data):
    ans=[]
    for t in data:
        v,spot=t['Portfolio']['Value'],t['Portfolio']['SpotPrcVol']
        a=t['IndexFutures']
        for i in a:
            i['OptimalHedgeRatio']=round(i["CoRelationCoefficient"]*spot/i["FuturePrcVol"],3)
            i["NumFuturesContract"]=i['OptimalHedgeRatio']*v/(i["IndexFuturePrice"]*i["Notional"])
        a.sort(key=lambda x:(x["NumFuturesContract"],x["OptimalHedgeRatio"]))
        ans.append({"HedgePositionName":a[0]["Name"],"OptimalHedgeRatio":a[0]["OptimalHedgeRatio"],"NumFuturesContract":int(a[0]["NumFuturesContract"]+0.5)})
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



