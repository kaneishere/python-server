"number_of_elements" : 4,
    "number_of_operations" : 2,
    "elements" :  "YyYy"

n = 4
m = 2
s = "1010"

def dfs(s, nowlevel, factor):
    tem = 0
    maxx = 0
    for i in range(len(s)):
        maxx = max(maxx, dfs(s[:i]+s[i+1:], nowlevel+1, factor/len(s)))
        if(s[i] == '1' or s[len(s)-1-i] == '1'):
            tem += 1
        
        
    