
import heapq

data = {'boardSize': 225, 'players': 6, 'jumps': ['0:185', '224:0', '51:125', '42:12', '183:0', '68:212', '74:0', '158:26', '0:105', '201:27', '146:139', '0:163', '132:0', '6:157', '0:45', '0:199', '69:149', '103:0', '0:194', '0:90', '0:98', '121:50', '167:0', '123:0', '77:86', '0:38', '151:109', '113:0', '0:47', '61:95', '191:223', '184:0', '73:93', '58:0', '0:171', '182:155', '180:192', '154:0', '0:24', '0:206', '156:0', '152:0', '131:198', '118:0', '55:0', '115:14', '205:0', '53:85', '0:3', '0:211', '143:36', '0:196', '0:18', '0:30', '80:0', '144:0', '64:11', '81:0', '0:23', '33:0', '177:0', '0:122', '217:63', '0:25']}
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

