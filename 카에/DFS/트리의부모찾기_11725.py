import sys
sys.stdin=open("input.txt", "r")
sys.setrecursionlimit(10**6)

node = int(input())
graph = [[] for _ in range(node+1)]
visited = [0 for _ in range(node+1)]
answer = [0 for _ in range(node+1)]

for _ in range(node-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(vertex):
    for next in graph[vertex]:
        if visited[next] == 0:
            visited[next] = 1
            answer[next] = vertex
            dfs(next)

dfs(1)
for i in range(2, node+1):
    print(answer[i])