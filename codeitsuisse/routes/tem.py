
import heapq

data = {'boardSize': 342, 'players': 7, 'jumps': ['149:325', '226:32', '260:296', '189:88', '120:85', '143:312', '121:0', '0:328', '0:34', '330:230', '109:58', '301:0', '0:247', '278:193', '0:300', '28:223', '0:317', '0:253', '0:179', '188:0', '334:0', '178:0', '54:24', '131:284', '13:0', '50:288', '7:0', '0:100', '269:8', '0:286', '108:0', '235:147', '0:194', '228:0', '0:304', '0:79', '0:192', '75:93', '0:276', '0:268', '151:306', '240:0', '173:60', '167:37', '277:0', '209:94', '134:171', '25:0', '320:0', '190:233', '0:77', '0:248', '213:186', '124:0', '62:200', '183:129', '0:4', '196:0', '0:191', '0:168', '57:0', '86:15', '176:116', '0:319', '302:0', '0:305', '0:256', '3:84', '80:89', '270:198', '0:12', '239:21', '132:159', '123:290', '289:145', '0:45', '275:0', '103:0', '0:315', '0:203', '0:150', '148:229', '9:244', '146:0', '41:227', '133:0', '101:217', '242:0', '292:5', '0:210', '118:0', '53:208', '245:115', '83:0', '14:0', '111:254', '321:11', '0:19', '43:33', '66:175', '336:0', '197:0', '309:0', '98:0', '231:0', '0:130', '122:0', '20:199', '0:135', '224:0', '0:51', '47:96', '195:104', '0:287', '202:291', '280:340', '236:65', '69:262', '257:0', '0:327', '61:0', '0:6', '318:18', '35:0', '158:0', '339:0', '52:0', '279:0', '204:68', '0:172', '63:67', '234:174', '0:303', '0:163', '0:106', '0:95', '42:0', '165:250', '261:0', '81:0', '238:0', '249:180', '259:71', '0:271', '316:161', '0:82', '27:0', '0:274', '0:17', '0:293', '92:243', '0:107', '144:0', '0:152', '90:311', '102:142', '307:282', '338:170', '215:112', '127:324', '117:0', '0:308', '0:331', '137:0', '273:0', '97:0', '39:0', '70:169']}
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

