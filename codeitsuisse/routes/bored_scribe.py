import logging
import json
from caesarcipher import CaesarCipher
from wordsegment import load, segment

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

def solve(data):
    res = []
    load()
    for dic in data:
        ans = {}
        i,s = dic['id'],dic['encryptedText']
        ans['id']=i
        cip = CaesarCipher(s)
        ori = cip.cracked
        offset = (26+ord(s[0])-ord(ori[0]))%26
        cnt,l,ind = 0,0,0
        for x in range(len(s)-1):
            for y in range(x+1,len(s)):
                tmp=ori[x:y+1]
                cur=y-x+1
                if tmp==tmp[::-1]:
                    if cur>l:
                        ind,l=x,cur
                    cnt+=1
        for c in ori[ind:ind+l]:
            cnt+=ord(c)
        for t in range(26):
            if cnt*t%26==offset:
                ans['encryptionCount'] = t
                break
        s = ' '.join(segment(ori))
        tmp = s.split(' ')
        p=0
        if 'palindrome' in tmp:
            if 'is' in tmp:
                iss=tmp.index('is')
                if tmp.index('palindrome')>iss:
                    for i in range(iss):
                        ttmp=''.join(tmp[i:iss])
                        if ttmp==ttmp[::-1]:
                            s=''
                            if i!=0:
                                s=' '.join(tmp[:i])+' '
                            s+=ttmp+' '+' '.join(tmp[iss:])
                            break
        ans['originalText'] = s
        res.append(ans)
    return res
@app.route('/bored-scribe', methods=['POST'])
def bored_scribe():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    result=solve(data)
    logging.info("My result :{}".format(result))
    return json.dumps(result);

'''
data=[ { "id": 1, "encryptedText": "oxzbzxofpxkbkdifpemxifkaoljb" } ]
print(solve(data))
'''

