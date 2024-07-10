import sys
n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

def dfs(v):
    visited[v] = True
    count = 1  # 현재 노드도 카운트
    for neighbor in graph[v]:
        if not visited[neighbor]:
            count += dfs(neighbor)
    return count

# 1번 컴퓨터에서 시작, 자기 자신 빼기 
result = dfs(1) - 1
print(result)