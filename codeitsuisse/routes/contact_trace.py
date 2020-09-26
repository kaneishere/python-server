import logging
import json
import random

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


memo = {}
origin = False
answers = []

def diff(a,b, name_to_genome): 
    # returns (cnt, non-silent)
    if a+b in memo:
        return memo[a+b]
    if b+a in memo:
        return memo[b+a]
    

    cnt = 0
    non_silent = 0
    a_l = name_to_genome[a].split('-')
    b_l = name_to_genome[b].split('-')
    for i in range(a_l):
        for j in range(3):
            if a_l[i][j] != b[i][j]:
                cnt += 1
                if j == 0:
                    non_silent += 1

    memo[a+b] = (cnt, non_silent > 1)
    return memo[a+b]


def dfs(explored_sets, cur_gene, ans, name_to_genome):

    explore = False
    to_explore = []
    mx = 10000000000000
    mn = mx
    print(answers)
    for key, value in explored_sets.items():
        if not value: continue
        cnt, non_silent = diff(cur_gene, key, name_to_genome)
        mn = min(mn, cnt)
    logging.info("minimum diff: {}".format(mn))
    if mn == mx:
        if len(ans) > 1:
            " -> ".join(ans)
            answers.append(ans)
        return 
        
    for key, value in explored_sets:
        if not value and diff(key, cur_gene, name_to_genome)[0] == mn:
            to_explore.append(key)
            explored_sets[key] = False
    
    for gene in to_explore:
        if diff(cur_gene, gene, name_to_genome)[1]:
            ans.append("*" + gene)
        else:
            ans.append(gene)
        dfs(explored_sets, gene, ans)
        ans.pop()



@app.route('/contact_trace', methods=['POST'])
def contact_trace():
    data = request.get_data() 

    logging.info("data from request {}".format(data))
    data = json.loads(data.decode('utf-8'))
    logging.info("data from request {}".format(data))
    # logging.info("data sent for evaluation {}".format(data))
    # random.seed() 
    # logging.info("My result :{}".format(result))
    
    answers.clear()
    memo.clear()
    origin = False

    infected = data["infected"]
    origin = data["origin"]
    cluster = data["cluster"]
    # m -> name, genome
    logging.info("data from cluster {}".format(cluster))
    name_to_gene = {}
    for c in cluster:
        name_to_gene[c['name']] = c['genome']

    name_to_gene[origin['name']] = origin['genome']
    
    explored = { key : False for key in name_to_gene.keys() }
    
    
    ans = [infected]


    dfs(explored, infected, ans, name_to_gene)
    return json.dumps(answers)



