
import heapq

data = {'boardSize': 342, 'players': 8, 'jumps': ['193:69', '19:280', '211:62', '184:0', '299:265', '0:98', '67:0', '189:0', '297:0', '0:159', '15:0', '204:222', '250:74', '219:0', '170:242', '59:169', '0:4', '191:0', '50:301', '0:3', '31:0', '144:0', '55:178', '196:298', '235:0', '0:155', '103:0', '173:129', '331:0', '0:126', '0:151', '0:231', '321:0', '0:165', '47:0', '0:224', '34:0', '256:226', '168:115', '259:0', '314:0', '139:253', '52:24', '326:0', '0:278', '82:0', '0:11', '203:0', '249:0', '306:106', '0:156', '114:340', '172:95', '46:0', '0:78', '21:194', '109:0', '337:77', '289:96', '48:0', '25:254', '118:0', '49:208', '51:0', '240:138', '122:192', '266:36', '66:190', '111:195', '0:79', '0:277', '0:143', '0:283', '218:0', '94:232', '175:112', '102:284', '0:336', '128:0', '270:0', '238:88', '320:0', '0:64', '17:273', '116:86', '308:263', '0:145', '183:147', '0:323', '206:131', '171:327', '0:33', '0:40', '83:166', '315:0', '110:182', '84:276', '291:37', '312:150', '272:0', '287:0', '158:0', '0:241', '328:164', '56:0', '179:117', '338:0', '0:318', '0:309', '0:2', '0:307', '207:0', '0:124', '0:177', '0:133', '0:10', '0:225', '146:229', '0:162', '0:99', '92:0', '257:0', '0:213', '217:313', '269:53', '157:0', '255:45', '76:0', '230:54', '0:130', '317:0', '0:97', '0:275', '227:205', '0:8', '251:228', '39:267', '135:288', '141:215', '160:167', '0:26', '68:0', '13:0', '85:264', '186:234', '274:0', '80:0', '258:319', '334:0', '282:149', '0:247', '0:153', '0:105', '246:61', '44:237', '296:0', '0:65', '0:180', '0:236', '35:87', '0:30', '0:311', '113:252', '210:60', '243:0', '341:43', '125:0', '101:29']}
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

