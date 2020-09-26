import logging
import json
import random
from collections import deque

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

UP = -1
DOWN = -2

best = []

def compare(cur, dest, dist, q, parent, i=0):
    if dist[cur] + 1 < dist[dest]:
        q.append(dest)
        dist[dest] = dist[cur] + 1
        if i: 
            parent[dest] = cur + i
            parent[cur+i] = cur
        else:
            parent[dest] = cur

def dfs(start, visited, n, rolls, jumps, cur_cost, mn):
    if cur_cost >= mn:
        return

    if start > n:
        start = n - (start - n)
    
    if start not in jumps:
        if cur_cost < mn:
            mn = cur_cost
            best = [i for i in rolls] 
        return 
    
    else: 
        if jumps[start] == UP:
            for i in range(1,7):
                dest = start + i
                if dest == n: continue
                rolls.append(i)
                if dest > n: dest = n - (dest - n)
                dfs(dest, visited, n, rolls,jumps, cur_cost + int(dest in visited), mn)
                rolls.pop()
            
        elif jumps[start] == DOWN:
            for i in range(1,7):
                rolls.append(i)
                dest = start - i
                if dest < 1: dest = 1 - dest 
                dfs(dest, visited, n, rolls,jumps, cur_cost + int(dest in visited), mn)
                rolls.pop()

        else:
            dfs(jumps[start], visited,n,rolls,jumps,cur_cost+int(jumps[start] in visited), mn)

    
    

def solve(data):
    n = data['boardSize']
    players = data['players']
    jumps = {}
    parent = [-1] * (n+1)
    for jump in data['jumps']:
        start, end = map(int, jump.split(':'))
        if start and end:
            jumps[start] = end
            
        elif start == 0:
            jumps[end] = DOWN 
        else:
            jumps[start] = UP

    logging.info("jumps {}".format(jumps))
    dist = [10000000000000000 for i in range(n+1)]
    q = deque([1])
    dist[1] = 0
    while len(q):
        cur = q.popleft()
        for i in range(1,7):
            if cur + i > n: continue
            if cur + i not in jumps:
                compare(cur, cur+i, dist, q, parent)
            
            else:
                if jumps[cur+i] == UP:
                    for j in range(1,7):
                        if cur + i + j <= n:
                            compare(cur, cur+i+j, dist, q, parent, i)
                
                elif jumps[cur+i] == DOWN:
                    for j in range(1, 7):
                        if cur + i - j >= 1:
                            compare(cur, cur + i - j, dist, q, parent, i) 

                else:
                    compare(cur, jumps[cur+i], dist, q, parent, i)

    logging.info("dist: {}".format(dist))
    box = n
    seq = []
    logging.info("parent: {}".format(parent))
    while box != -1:
        seq.append(box)
        box = parent[box]

    seq.reverse()
    visited = set(seq)
    logging.info("sequence: {}".format(seq))
    ret = []

    prv_jmp = False 
    for i in range(1,len(seq)):
        # first one must be one
        if not prv_jmp:
            ret += [0] * (players-1)
            prv_jmp = seq[i] in jumps
        
        if seq[i] != n:
            ret.append(seq[i] - seq[i-1])
        # print(ret)
        # logging.info("seq[i] {}".format(seq[i]))
            j = len(ret) - 2
            fill = ret[len(ret)-1] 
            while j >= 0 and ret[j] == 0:
                ret[j] = fill
                j -= 1

        elif seq[i] == n:
            start = seq[i-1]
            mn = 1000000000000000000000000
            dfs(start, visited, n, [], jumps, 0, mn)

            logging.info("best: {}".format(best))             


                     



    logging.info("ret: {}".format(ret))
    



@app.route('/slsm', methods=['POST'])
def slsm():
    data = request.get_data() 

    data = json.loads(data.decode('utf-8'))
    # logging.info("data from request {}".format(data))
    solve(data) 

    # return json.dumps(answers)
    return ""



