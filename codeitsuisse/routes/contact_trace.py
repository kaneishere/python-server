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
    # logging.info("a + b {}".format(a+b))
    if a+b in memo:
        return memo[a+b]
    if b+a in memo:
        return memo[b+a]
    

    cnt = 0
    non_silent = 0
    a_l = name_to_genome[a].split('-')
    b_l = name_to_genome[b].split('-')
    # logging.info("a_l: {}".format(a_l))
    for i in range(len(a_l)):
        for j in range(3):
            if a_l[i][j] != b_l[i][j]:
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
    # logging.info("explored_sets: {}".format(explored_sets))
    for key, value in explored_sets.items():
        if value: continue
        cnt, non_silent = diff(cur_gene, key, name_to_genome)
        mn = min(mn, cnt)
    # logging.info("minimum diff: {}".format(mn))
    # logging.info("ans: {}".format(ans))
    if mn == mx:
        if len(ans) > 1:
            
            answers.append(" -> ".join(ans))
        return 
        
    for key, value in explored_sets.items():
        if not value and diff(key, cur_gene, name_to_genome)[0] == mn:
            to_explore.append(key)
            explored_sets[key] = True 
    
    # logging.info("to_explore: {}".format(to_explore))
    for gene in to_explore:
        non_silent = False
        if diff(cur_gene, gene, name_to_genome)[1]:
            non_silent = True
            prv = ans.pop()
            ans.append("*" + prv)
            ans.append(gene)
        else:
            ans.append(gene)
        dfs(explored_sets, gene, ans, name_to_genome)
        ans.pop()
        if non_silent:
            ans.pop()
            ans.append(cur_gene)



@app.route('/contact_trace', methods=['POST'])
def contact_trace():
    data = request.get_data() 

    # logging.info("data from request {}".format(data))
    data = json.loads(data.decode('utf-8'))
    # logging.info("data from request {}".format(data))
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
    name_to_gene[infected['name']] = infected['genome']
    logging.info("data from name_to_gene {}".format(name_to_gene)) 

    explored_sets = {}
    for key, value in name_to_gene.items():
        if key != infected['name']:
            explored_sets[key] = False
    
    
    ans = [infected['name']]


    dfs(explored_sets, infected['name'], ans, name_to_gene)
    logging.info("data: {}".format(data))
    logging.info("answers: {}".format(answers))
    return json.dumps(answers)



