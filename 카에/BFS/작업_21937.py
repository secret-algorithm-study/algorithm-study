import sys
sys.stdin=open("input.txt", "r")
from collections import deque

n, m = map(int, input().split())
jobs = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
q = deque()

# 부모 노드 저쟝
for _ in range(m):
  a, b = map(int, input().split())
  jobs[b].append(a)

x = int(input())
q.append(x)
visited[x] = True
cnt = 0
while q:
  node = q.popleft()
  for next_node in jobs[node]:
    if visited[next_node] == False:
      visited[next_node] = True
      cnt += 1
      q.append(next_node)

print(cnt)
