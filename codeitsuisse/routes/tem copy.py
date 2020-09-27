
n = 4
m = 2
s = "1010"

tt = 1
for i in range(m):
    tt*=(n-i)

def dfs(s, nowlevel, factor):
    if(nowlevel == m):
        return 0
    maxx = 0
    tem = []
    for i in range(len(s)):
        x = (1 if (s[i] == '1') else 0)
        tem.append(tt*x + dfs(s[:i]+s[i+1:], nowlevel+1, 1/(len(s)-1)))
    #print(tem)
    for i in range(len(s)):
        maxx += max(tem[i], tem[len(s)-1-i])
        
    return factor*maxx
        
print(dfs(s, 0, 1/len(s))/tt)        
    