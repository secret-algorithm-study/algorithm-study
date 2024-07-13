n,m = map(int, input().split())

vs = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    vs[b].append(a)

def bfs(i):
    q = [i]
    vst = [0]*(n+1)
    cnt = 1
    while q:
        t = q.pop(0)
        for v in vs[t]:
            if vst[v]: continue
            q.append(v)
            vst[v] = 1
            cnt += 1
    return cnt


cnts = [0]
for i in range(1, n+1):
    cnt = bfs(i)
    cnts.append(cnt)
    
max_cnt = max(cnts)

idxs = [i for i,v in enumerate(cnts) if v == max_cnt]
print(*sorted(idxs))

# 시간초과