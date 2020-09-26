import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

def solve(data):
    ans = []
    shape = data.get("shapeCoordinates")
    line = data.get("lineCoordinates")
    l2=((line[0]['x'],line[0]['y']),(line[1]['x'],line[1]['y']))
    n=len(shape)
    if n==1:
        x=shape[0]['x']
        y=shape[0]['y']
        if x==l2[1][0] and y==l2[1][1] or x==l2[0][0] and y==l2[0][1] or x!=l2[1][0] and x!=l2[0][0] and (l2[1][1]-y)/(l2[1][0]-x)==(l2[0][1]-y)/(l2[0][0]-x):
            return shape

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]
    for i in range(n):
        j=(i+1)%n
        
        l1=((shape[i]['x'],shape[i]['y']),(shape[j]['x'],shape[j]['y']))

        x = (l1[0][0] - l1[1][0], l2[0][0] - l2[1][0])
        y = (l1[0][1] - l1[1][1], l2[0][1] - l2[1][1])

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(x, y)
        if div == 0:
            continue
        d = (det(*l1), det(*l2))
        x = det(d, x) / div
        y = det(d, y) / div
        if (l1[0][0]-x)*(l1[1][0]-x)<=0 and (l1[0][1]-y)*(l1[1][1]-y)<=0:
            ans.append((round(x,2),round(y,2)))
    ans=list(set(ans))
    res=[{'x':i[0],'y':i[1]} for i in ans]
    return res

@app.route('/revisitgeometry', methods=['POST'])
def revisitgeometry():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    result=solve(data)
    logging.info("My result :{}".format(result))
    return json.dumps(result);

'''
data = {
  "shapeCoordinates": [
    { "x": 21, "y": 70 },
    { "x": 72, "y": 70 },
    { "x": 72, "y": 127 }
  ],
  "lineCoordinates": [
    { "x": -58, "y": 56 },
    { "x": -28, "y": 68 }
  ]
}
print(solve(data))
'''


