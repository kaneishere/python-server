import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

def f(n,m,s):
    tt = 1
    for i in range(m):
        tt*=(n-i)

    def dfs(s, nowlevel, factor):
        if(nowlevel == m):
            return 0
        maxx = 0
        tem = [0 for i in range(len(s))]
        for i in range(len(s)):
            x = (1 if (s[i] == 'Y') else 0)
            if (s[i]=='Y' and s[len(s)-1-i]=='y'):
                tem[i]=tt*x + dfs(s[:i]+s[i+1:], nowlevel+1, 1/(len(s)-1))
                tem[len(s)-1-i]=tmp[i]
            else if (s[i]=='y' and s[len(s)-1-i]=='Y'):
                continue
            else:
                tem[i]=tt*x + dfs(s[:i]+s[i+1:], nowlevel+1, 1/(len(s)-1))
        #print(tem)
        for i in range(len(s)):
            maxx += max(tem[i], tem[len(s)-1-i])
            
        return factor*maxx
            
    return (dfs(s, 0, 1/len(s))/tt)     

@app.route('/yin-yang', methods=['POST'])
def evaluate_yinyang():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))

    n = data.get("number_of_elements")
    m = data.get("number_of_operations")
    s = data.get("elements")
    
     
    result = {'result':f(n,m,s)}
    logging.info("My result :{}".format(result))
    return json.dumps(result)

