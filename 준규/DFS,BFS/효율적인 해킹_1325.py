import sys
from collections import deque
sys.stdin=open("input.txt", "r")

n, m = map(int, input().split())

relation = [[] for i in range(n)]
result = [0 for i in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    relation[y-1].append(x-1)

for i in range(n):
    visited = [False] * n
    queue = deque([i])
    visited[i] = True

  
    while queue:
        value = queue.popleft()
        result[i] += 1

        for neighbor in relation[value]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True



max_value = max(result)
for i in range(n):
    if result[i] == max_value:
        print(i + 1, end=" ")