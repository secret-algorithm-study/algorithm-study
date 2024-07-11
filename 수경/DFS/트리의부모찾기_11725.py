n = int(input())

vs = [[] for _ in range(n+1)]
ps = [0]*(n+1)

for _ in range(n-1):
  a,b = map(int,input().split())
  vs[a].append(b)
  vs[b].append(a)

q = [1]
while q:
  t = q.pop(0)
  for v in vs[t]:
    if ps[v]: continue
    ps[v] = t
    q.append(v)

for p in ps[2:]: print(p)