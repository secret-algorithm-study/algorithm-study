from collections import deque
from sys import stdin
input = stdin.readline


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)


def bfs(v):
    queue = deque([v])
    cnt = 0
    visited = [False] * (n+1)
    visited[v] = True
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                cnt += 1
    return cnt

# 5번 작업을 하기 위해 먼저 해야하는 작업의 개수
x = int(input())
print(bfs(x))

