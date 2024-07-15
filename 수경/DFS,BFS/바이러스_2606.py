n = int(input())
e = int(input())

g = [[] for _ in range(n+1)]
vst = [0]*(n+1)

for _ in range(e):
  a,b = map(int, input().split())
  g[a].append(b)
  g[b].append(a)


def dfs(v):
  vst[v] = 1
  for _v in g[v]:
    if vst[_v]==1: continue
    dfs(_v)

dfs(1)
print(sum(vst)-1)