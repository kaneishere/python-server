
import heapq

data = {'boardSize': 342, 'players': 7, 'jumps': ['20:0', '329:141', '106:0', '309:105', '270:0', '45:218', '74:184', '0:129', '161:0', '325:0', '69:259', '240:36', '0:39', '137:0', '0:154', '78:0', '83:0', '0:331', '131:0', '282:109', '0:239', '0:299', '103:0', '269:48', '187:125', '0:193', '279:0', '205:0', '0:118', '316:85', '15:229', '289:70', '0:126', '275:0', '0:318', '233:0', '0:25', '223:314', '0:267', '86:250', '12:0', '0:268', '97:0', '0:224', '263:241', '117:149', '0:50', '110:335', '0:168', '317:115', '0:334', '190:0', '227:0', '277:121', '13:200', '75:44', '0:156', '93:256', '155:176', '151:177', '17:143', '153:0', '0:315', '88:0', '336:194', '122:0', '0:128', '46:51', '322:301', '0:303', '328:0', '298:0', '0:28', '166:320', '67:0', '265:211', '130:0', '192:29', '0:41', '235:62', '339:0', '292:0', '0:99', '0:291', '323:120', '87:0', '271:133', '195:150', '0:59', '104:254', '72:26', '0:34', '0:185', '0:183', '134:0', '73:258', '158:136', '278:0', '142:307', '2:243', '264:94', '0:116', '160:0', '6:181', '0:220', '293:102', '198:33', '114:165', '196:0', '197:0', '0:53', '327:81', '283:0', '0:173', '57:225', '230:0', '0:244', '201:0', '0:294', '0:68', '140:222', '186:89', '40:0', '108:119', '214:0', '217:237', '337:0', '232:0', '286:0', '204:63', '52:0', '0:210', '203:0', '228:212', '182:234', '43:221', '0:296', '132:333', '0:285', '0:167', '0:60', '0:113', '111:0', '27:226', '3:341', '295:127', '0:199', '24:0', '245:159', '0:16', '0:91', '208:54', '0:189', '58:0', '80:0', '0:112', '238:14', '37:247', '0:288', '169:313', '0:300', '306:96', '7:0', '82:170', '231:310', '272:0', '0:55', '174:0']}
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