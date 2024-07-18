import sys
sys.stdin = open('input.txt', 'r');

n = int(input())
matrix = []
num = []

for i in range(n):
    matrix.append(list(map(int, input())))
count = 0
result = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    
    current = matrix[x][y]
    if current == 1:
        global count
        count += 1
        #탐색한 곳은 0 초기화
        matrix[x][y] = 0;
        
        #상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True
    return False




for i in range(n):
    for j in range(n):
        if DFS(i, j) == True:
            num.append(count)
            result += 1
            count = 0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])