import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

def findcluster(grid):
    n = len(grid)
    m = len(grid[0])

    def valid(i, j):
        return (i >= 0 and i < n and j >= 0 and j < m)

    def dfs(i, j):
        grid[i][j] = "*"
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if(valid(i+di, j+dj) and grid[i+di][j+dj] != "*"):
                    dfs(i+di, j+dj)

    ans = 0
    for i in range(n):
        for j in range(m):
            if(grid[i][j] == "1"):
                dfs(i, j)
                ans+=1

    print("Ans:", ans)
    return ans

@app.route('/cluster', methods=['POST'])
def evaluate_cluster():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))

    # inputValue = data.get("list")

    ans = {"answer": findcluster(data)}
    return jsonify(ans);



