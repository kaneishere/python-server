circles = (451, 0)
buckets = [[(435, 4), (435, 106), (464, 106), (464, 4)], [(358, 450), (358, 608), (394, 608), (394, 450)], [(23, 999), (23, 1009), (32, 1009), (32, 999)], [(435, 347), (435, 359), (438, 359), (438, 347)], [(459, 111), (459, 222), (486, 222), (486, 111)], [(534, 1152), (534, 1212), (717, 1212), (717, 1152)], [(316, 847), (316, 1001), (368, 1001), (368, 847)], [(365, 613), (365, 766), (443, 766), (443, 613)], [(78, 19), (78, 70), (149, 70), (149, 19)], [(368, 316), (368, 444), (451, 444), (451, 316)]]
pipes = [[(455, 302), (447, 310)], [(292, 1003), (319, 1030)], [(282, 1179), (310, 1207)], [(318, 804), (357, 843)], [(204, 1601), (245, 1642)], [(639, 8), (644, 13)], [(322, 1210), (304, 1228)], [(173, 574), (164, 583)], [(286, 1234), (310, 1258)], [(344, 1116), (307, 1153)], [(321, 1155), (302, 1174)], [(363, 1086), (339, 1110)], [(324, 1035), (316, 1043)], [(511, 1081), (538, 1108)], [(863, 1140), (849, 1154)], [(413, 262), (451, 300)], [(101, 348), (63, 386)], [(480, 225), (448, 257)], [(313, 1047), (350, 1084)], [(377, 771), (348, 800)]]

IMG_SIZE = 0
for b in buckets:
    for bb in b:
        IMG_SIZE = max(IMG_SIZE, bb[0], bb[1])

for b in pipes:
    for bb in b:
        IMG_SIZE = max(IMG_SIZE, bb[0], bb[1])

img = [[-1 for i in range(IMG_SIZE+5)] for j in range(IMG_SIZE+5)]
G = [list() for j in range(len(buckets)+5)]
area = [0 for j in range(len(buckets)+5)]


for b in range(len(buckets)):

    buc = buckets[b]
    left, right, top, bottom = buc[0][0], buc[2][0], buc[0][1], buc[2][1]

    if(left > right):
        buc[0], buc[2] = buc[2], buc[0]
        buc[1], buc[3] = buc[3], buc[1]
        left, right = right, left

    for i in range(top, bottom+1):
        
        img[left][i] = b
        img[right][i] = b
    for i in range(left, right+1):
        img[i][bottom] = b
    area[b] = (right-left-1)*(bottom-top)
    

for pipe in pipes:
    up, down = pipe
    src, tgt = -1, -1
    if(up[1] > down[1]):
        up, down = down, up
    for i in range(up[1], -1, -1):
        if(img[up[0]][i] != -1):
            src = img[up[0]][i]
            break
    for i in range(down[1], IMG_SIZE):
        if(img[down[0]][i] != -1):
            tgt = img[down[0]][i]
            break
    if(src != -1 and tgt != -1):
        G[src].append(tgt)

startbuc = -1
for i in range(circles[1], IMG_SIZE):
    if(img[circles[0]][i] != -1):
        startbuc = img[circles[0]][i]
        break

for b in range(len(buckets)):
    buc = buckets[b]
    left, right, top, bottom = buc[0][0], buc[2][0], buc[0][1], buc[2][1]
    tgt = -1

    for i in range(bottom+1, IMG_SIZE):
        if(img[left][i] != -1):
            tgt = img[left][i]
            break

    if(tgt != -1):
        G[b].append(tgt)

    tgt = -1
    
    for i in range(bottom+1, IMG_SIZE):
        if(img[right][i] != -1):
            tgt = img[right][i]
            break
    
    if(tgt != -1):
        G[b].append(tgt)


if(startbuc == -1):
    print(0)
    ##############################

visited = [0 for j in range(len(buckets)+5)]
def dfs(v):
    visited[v] = 1
    for to in G[v]:
        if visited[to]==0:
            dfs(to)
        
img = [[-1 for i in range(IMG_SIZE+5)] for j in range(IMG_SIZE+5)]
for b in range(len(buckets)):
    buc = buckets[b]
    left, right, top, bottom = buc[0][0], buc[2][0], buc[0][1], buc[2][1]
    for j in range(top, bottom):
        for i in range(left+1, right):
            if (img[i][j]==-1) or (img[i][j]!=-1 and area[img[i][j]]<area[b]):
                img[i][j] = b

dfs(startbuc)

ans =0

for i in range(IMG_SIZE):
    for j in range(IMG_SIZE):
        if img[i][j]!=-1 and visited[img[i][j]]==1:
                ans += 1



print(visited)    
print(G)
print("ans", ans)
