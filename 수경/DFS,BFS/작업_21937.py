n,m = map(int,input().split())

g = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    g[b].append(a)
    
x = int(input())

def dfs(x):
    s = [x]
    v = []
    cnt = 0
    while s:
        t = s.pop()
        if t in v: continue
        v.append(t)
        s.extend(g[t])
        cnt += 1
    return cnt-1

print(dfs(x))