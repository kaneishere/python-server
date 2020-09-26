import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


def processstring(str):
    cnt = {}
    cnt['A'] = 0
    cnt['C'] = 0
    cnt['G'] = 0
    cnt['T'] = 0

    for i in str:
        cnt[i] += 1

    #AAA -10 CC +25 ACGT +15

    print(cnt)

    numACGT = cnt[min(cnt)]
    numCC = cnt['C']//2


    maxx = -10000000000
    for i in range(numACGT    +1):
        for j in range((cnt['C']-i)//2    +1):
            remainA = cnt['A']-i
            remainElse = cnt['A']+cnt['T']+cnt['C']+cnt['G']-4*i-2*j-remainA

            moreA = remainA - 2 - i - 2*j
            deduct = 0
            if(moreA > 0):
                deduct = 10
                moreA -= 1

                deduct += (moreA//3)*10
            
                

            score = i*15 + j*25 - deduct

            if(score > maxx):
                maxx = max(score, maxx)
                maxi = i
                maxj = j            
            
            
    remainA = cnt['A'] - maxi
    ans = ""

    for i in range(maxi):
        frontA = min(remainA, 1)
        ans += 'A'*frontA + 'ACGT'
        remainA -= frontA

    for i in range(maxj):
        frontA = min(remainA, 2)
        ans += 'A'*frontA + 'CC'
        remainA -= frontA

    cnt['A'] -= maxi
    cnt['T'] -= maxi
    cnt['C'] -= maxi
    cnt['G'] -= maxi
    cnt['C'] -= (maxj*2)


    for i in range(cnt['C']):
        frontA = min(remainA, 2)
        ans += 'A'*frontA + 'C'
        remainA -= frontA

    for i in range(cnt['T']):
        frontA = min(remainA, 2)
        ans += 'A'*frontA + 'T'
        remainA -= frontA
        
    for i in range(cnt['G']):
        frontA = min(remainA, 2)
        ans += 'A'*frontA + 'G'
        remainA -= frontA


    ans += 'A'*remainA

    print(ans)
    return ans

@app.route('/intelligent-farming', methods=['POST'])
def evaluate_GMO():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))

    inputValue = data.get("list")

    for i in range(len(inputValue)):
        inputValue[i]['geneSequence'] = processstring(inputValue[i]['geneSequence'])

    # logging.info("My result :{}".format(result))
    return jsonify(data);



