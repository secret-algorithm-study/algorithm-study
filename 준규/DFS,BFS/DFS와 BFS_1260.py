import sys
from collections import deque
sys.stdin=open("input.txt", "r")

n,m,v = map(int,input().split())

graph = [[] for _ in range(n+1)];

visit1 = [0]*(n+1)
visit2 = [0]*(n+1)

result1 = []
result2 = []

for i in range (m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()



def DFS(v) : 
    visit1[v] = 1
    result1.append(v)

    for i in graph[v]:
        if visit1[i] == 0:
            DFS(i)    


def BFS(v):
    queue = deque([v])
    
    visit2[v] = 1

    while queue:
        node = queue.popleft()
      
        result2.append(node)

        for i in graph[node]:
            if visit2[i] == 0:
                queue.append(i)
                visit2[i] = 1


DFS(v)
print(" ".join(map(str, result1)))


BFS(v)
print(" ".join(map(str, result2)))
