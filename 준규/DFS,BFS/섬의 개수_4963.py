import sys
sys.stdin=open("input.txt", "r")
sys.setrecursionlimit(1000000)

dx = [-1,-1,0,1,1,1,0,-1];
dy = [0,1,1,1,0,-1,-1,-1];


def isVisit(x,y):
    return visit[x][y] == 1;

def dfs(x,y):
    visit[x][y] = 1;

    for i in range(8):
        nx = x + dx[i];
        ny = y + dy[i];
        if 0 <= nx < h and 0 <= ny < w:
            neighbor = matrix[nx][ny];
            if neighbor == 1 and not isVisit(nx,ny):
                dfs(nx,ny);
        

while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:break;


    matrix = [];
    visit = [[0] * w for _ in range(h)];
    answer = 0;
    
    for i in range(h):
        matrix.append(list(map(int, input().split())))
    
    for x in range(h):
        for y in range(w):
            current = matrix[x][y];
            isVisited = isVisit(x,y);
            if current == 1 and not isVisited:
                dfs(x,y)
                answer += 1;
            
    
    print(answer);

