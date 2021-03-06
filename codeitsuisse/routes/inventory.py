import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

def findsol(str1, str2):
    dp =[ [(0,"") for i in range(len(str2)+5)] for j in range(len(str1)+5)]
    for m in range(len(str1) + 1):
        for n in range(len(str2) + 1):

            if m == 0:
                dp[m][n] =  (n,  ''.join(["+"+c for c in str2[:n]]))
            elif n == 0:
                dp[m][n] =  (m,  ''.join(["-"+c for c in str1[:m]]))
            elif (str1[m-1] == str2[n-1]):
                tem = dp[m-1][n-1]
                dp[m][n] = (tem[0], tem[1]+str2[n-1])
            else:
                tem1 = dp[m][n-1]
                tem2 = dp[m-1][n]
                tem3 = dp[m-1][n-1]


                dp[m][n] = min((1+tem1[0], tem1[1]+"+"+str2[n-1]), # Insert 
                            (1+tem2[0], tem2[1]+"-"+str1[m-1]), # Remove 
                            (1+tem3[0],tem3[1]+str2[n-1]) # Replace 
                            ) 

    return dp[len(str1)][len(str2)]

@app.route('/inventory-management', methods=['POST'])
def evaluate_inventory():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = []

    for d in data:
        source = d.get("searchItemName")
        temsource = source
        items = d.get("items")

        source = source.upper()
        items = [i.upper() for i in items]

        sol = [findsol(source, i) for i in items]
        sol = [(sol[i][0], items[i], sol[i][1]) for i in range(len(sol))]
        sol.sort()
        sol = [i[2] for i in sol][:10]

        # for i in range(len(sol)):
        #     ans = sol[i].split()
        #     for j in range(len(ans)):
        #         if(ans[j][0] == '+' or ans[j][0] == '-'):
        #             ans[j] = ans[j][0] + ans[j][1:].capitalize()
        #         else:
        #             ans[j] = ans[j].capitalize()

        #     sol[i] = ' '.join(ans)

        result.append({"searchItemName":temsource, "searchResult":sol})

    logging.info("My result :{}".format(result))
    return json.dumps(result)

