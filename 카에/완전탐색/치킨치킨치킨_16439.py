import sys
sys.stdin=open("input.txt", "r")

n, m = map(int, input().split())
members = [list(map(int, input().split())) for _ in range(n)]

answer = 0

def dfs(depth, start, picked_chicken_idx):
    global answer
    if depth == 3:
        total = 0
        for i in range(n):
            tmp = 0
            for chicken_idx in picked_chicken_idx:
                if tmp < members[i][chicken_idx]:
                    tmp = members[i][chicken_idx]
            total += tmp
        answer = max(answer, total)
    else:
        for i in range(start, m):
            dfs(depth+1, i+1, picked_chicken_idx+[i])

dfs(0, 0, [])
print(answer)            
