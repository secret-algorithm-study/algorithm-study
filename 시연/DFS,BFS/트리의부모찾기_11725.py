import sys
sys.setrecursionlimit(10**7) # 100000 정도에선 터짐
input = sys.stdin.readline

n = int(input()) 

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
parent = [0 for _ in range(n + 1)] 

for _ in range(n - 1):  # 트리의 간선 수는 노드 수 - 1
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    visited[node] = True
    for neighbor in graph[node]: # 인접 노드들에 대해 
        if not visited[neighbor]: # 방문하지 않은 노드라면
            parent[neighbor] = node # 부모 노드를 기록, neighbor의 부모는 node
            dfs(neighbor) 

dfs(1) 

for i in range(2, n + 1):
    print(parent[i])
