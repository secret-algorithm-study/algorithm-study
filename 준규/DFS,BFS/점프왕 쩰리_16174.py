import sys
sys.stdin = open('input.txt', 'r');

n = int(input());

maze = [list(map(int, input().split())) for _ in range(n)];

visit = [[0]*n for _ in range(n)];


dx = [1,0];
dy = [0,1];

def DFS(x,y):
    visit[x][y] = 1;

    for i in range(2):
        next_x = x + dx[i] * maze[x][y];
        next_y = y + dy[i] * maze[x][y];

        if 0<= next_x < n and 0 <= next_y < n:
            next_value = maze[next_x][next_y];
            if visit[next_x][next_y] == 0 :
                if next_value == -1:
                    print('HaruHaru');
                    exit(0);
                else:
                    DFS(next_x, next_y);
    return False;

DFS(0,0);
print('Hing');
