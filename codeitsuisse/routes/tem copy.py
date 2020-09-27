circles = (500, 0)
buckets = [[(360, 175), (360, 225), (400, 225), (400, 175)], [(480, 5), (480, 40), (520, 40), (520, 5)]]
pipes = [[(500, 50), (400, 150)]]


IMG_SIZE = 2048
img = [[-1 for i in range(IMG_SIZE+5)] for j in range(IMG_SIZE+5)]
G = [list() for j in range(len(buckets)+5)]
area = [0 for j in range(len(buckets)+5)]

for b in range(len(buckets)):

    buc = buckets[b]
    left, right, top, bottom = buc[0][0], buc[2][0], buc[0][1], buc[2][1]

    if(left > right):
        buc[0], buc[2] = buc[2], buc[0]
        buc[1], buc[3] = buc[3], buc[1]

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
    for i in range(down[1], 2049):
        if(img[down[0]][i] != -1):
            tgt = img[down[0]][i]
            break
    if(src != -1 and tgt != -1):
        G[src].append(tgt)

startbuc = -1
for i in range(circles[1], 2049):
    if(img[circles[0]][i] != -1):
        startbuc = img[circles[0]][i]
        break

for b in range(len(buckets)):
    buc = buckets[b]
    left, right, top, bottom = buc[0][0], buc[2][0], buc[0][1], buc[2][1]
    tgt = -1

    for i in range(bottom+1, 2049):
        if(img[left][i] != -1):
            tgt = img[left][i]
            break

    if(tgt != -1):
        G[b].append(tgt)

    tgt = -1
    
    for i in range(bottom+1, 2049):
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

for i in range(2049):
    for j in range(2049):
        if img[i][j]!=-1 and visited[img[i][j]]==1:
                ans += 1



print(visited)    
print(G)
print("ans", ans)

def(circle, bucket, pipe):
    IMG_SIZE = 2048
    img = [[-1 for i in range(IMG_SIZE+5)] for j in range(IMG_SIZE+5)]
    G = [list() for j in range(len(buckets)+5)]
    area = [0 for j in range(len(buckets)+5)]

    for b in range(len(buckets)):

        buc = buckets[b]
        left, right, top, bottom = buc[0][0], buc[2][0], buc[0][1], buc[2][1]

        if(left > right):
            buc[0], buc[2] = buc[2], buc[0]
            buc[1], buc[3] = buc[3], buc[1]

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
        for i in range(down[1], 2049):
            if(img[down[0]][i] != -1):
                tgt = img[down[0]][i]
                break
        if(src != -1 and tgt != -1):
            G[src].append(tgt)

    startbuc = -1
    for i in range(circles[1], 2049):
        if(img[circles[0]][i] != -1):
            startbuc = img[circles[0]][i]
            break

    for b in range(len(buckets)):
        buc = buckets[b]
        left, right, top, bottom = buc[0][0], buc[2][0], buc[0][1], buc[2][1]
        tgt = -1

        for i in range(bottom+1, 2049):
            if(img[left][i] != -1):
                tgt = img[left][i]
                break

        if(tgt != -1):
            G[b].append(tgt)

        tgt = -1
        
        for i in range(bottom+1, 2049):
            if(img[right][i] != -1):
                tgt = img[right][i]
                break
        
        if(tgt != -1):
            G[b].append(tgt)


    if(startbuc == -1):
        return 0
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

    for i in range(2049):
        for j in range(2049):
            if img[i][j]!=-1 and visited[img[i][j]]==1:
                    ans += 1



    print(visited)    
    print(G)
    return ans