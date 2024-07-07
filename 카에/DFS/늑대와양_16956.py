import sys
sys.stdin=open("input.txt", "r")

r, c = map(int, input().split())

farm = [list(input().replace('.', 'D')) for _ in range(r)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(r):
  for j in range(c):
    if farm[i][j] == 'W':
      for k in range(4):
        nx = dx[k]+i
        ny = dy[k]+j

        if nx >= 0 and ny >= 0 and nx < r and ny < c:
          if farm[nx][ny] == 'S':
            print(0)
            exit()

print(1)
for i in farm:
  print(*i, sep='')