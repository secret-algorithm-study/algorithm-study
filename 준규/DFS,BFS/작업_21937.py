# import sys
# sys.stdin = open('input.txt', 'r');
# sys.setrecursionlimit(10*7)
# n , m = map(int, input().split());

# node = [[] for _ in range(n+1)];

# visited = [0] * (n+1);

# for _ in range(m):
#     a, b = map(int, input().split());
#     node[b].append(a);

# x = int(input());



# def DFS(v):
    
#     visited[v] = 1;
#     for i in node[v]:
#         if visited[i] == 0:
            
#             DFS(i);

# DFS(x);

# print(sum(visited)-1);





import sys
sys.stdin = open('input.txt', 'r');

n , m = map(int, input().split());

node = [[] for _ in range(n+1)];

visited = [0] * (n+1);

for _ in range(m):
    a, b = map(int, input().split());
    node[b].append(a);

x = int(input());

def DFS(start):
    stack = [start]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            for i in node[v]:
                if not visited[i]:
                    stack.append(i)

DFS(x);

print(sum(visited)-1);
