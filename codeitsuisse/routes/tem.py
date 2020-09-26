
import heapq

data = {'boardSize': 90, 'players': 3, 'jumps': ['78:8', '16:51', '32:87', '0:77', '49:21', '0:83', '46:41', '25:58', '45:0', '35:0', '73:34', '28:31']}
boardSize = data.get("boardSize")
players = data.get("players")
jumps = data.get("jumps")

G = {i:{} for i in range(1,boardSize+1)}
laddersnake = {}
isjumppoint = [0 for i in range(boardSize+5)]

for jp in jumps:
    s, e = jp.split(':')
    s, e = int(s), int(e)
    if(s == 0):
        for i in range(1,7):
            G[e][s+i] = 0
        isjumppoint[e] = 1
    elif(e == 0):
        for i in range(1,7):
            G[s][s-i] = 0
        isjumppoint[s] = 1
    else:
        G[s][e] = 0
        laddersnake[s] = e
        isjumppoint[s] = 1

for i in range(1, boardSize):
    if(isjumppoint[i]):
        continue
    for j in range(1,7):
        if(i+j > boardSize):
            break
        G[i][i+j] = 1



def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0
    previous = {vertex: -1 for vertex in graph}

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous


distances, previous = calculate_distances(G, 1)

ans = []
path = [boardSize]
shortpath = []
now = boardSize
while True:
    pre = previous[now]
    if(pre==-1):
        break
    if(laddersnake.get(pre,0)!=now):
        ans.append(abs(now-pre))
        shortpath.append(now)
    now = pre
    path.append(now)

print(G)
print(ans[::-1])
    
print(path[::-1])

print(shortpath[::-1])

