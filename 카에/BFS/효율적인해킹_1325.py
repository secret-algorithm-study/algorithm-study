import sys
sys.stdin=open("input.txt", "r")
from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(vertex):
    q = deque([vertex])
    visited = [0]*(n+1)
    visited[vertex] = 1

    cnt = 1

    while q:
        vertex = q.popleft()

        for node in graph[vertex]:
            if visited[node] == 0:
                visited[node] = 1
                cnt += 1
                q.append(node)
    return cnt

results = []
max_val = -1

for i in range(1, n+1):
    result = bfs(i)
    if result > max_val:
        results = [i]
        max_val = result
    elif result == max_val:
        results.append(i)

print(*results)