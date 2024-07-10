import sys
sys.stdin=open("input.txt", "r")

sys.setrecursionlimit(10**6)

n = int(input())

node = [[] * (n+1) for _ in range(n+1)]

parent = [0] * (n+1)

for i in range(n-1):
    a,b = map(int,input().split())
    node[a].append(b)
    node[b].append(a)



def DFS(v):
    for i in node[v]:
        if parent[i] == 0:
            parent[i] = v
            DFS(i)

DFS(1)

for i in range(2, n+1):
    print(parent[i])


