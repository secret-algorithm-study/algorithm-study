import sys
sys.stdin = open('input.txt', 'r');

r, c, n = map(int, input().split())
arr = [list(input()) for _ in range(r)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
bombs = []


# 폭탄 위치 찾기
def finder(li):
    bombs = []
    for i in range(r):
        for j in range(c):
            if li[i][j] == 'O':
                bombs.append((i, j))
    return bombs


# 폭탄 터뜨리기
def bang():
    global arr, bombs
    for bx, by in bombs:
        arr[bx][by] = '.'
        # 상하 좌우 폭탄 터뜨리기
        for i in range(4):
            nx, ny = bx + direction[i][0], by + direction[i][1]
            if nx in range(r) and ny in range(c):
                arr[nx][ny] = '.'

# 폭탄으로 채우기
def bombFill(): 
    global arr
    arr = [['O'] * c for _ in range(r)]

# 결과 출력
def printer(list): 
    for line in list:
        print(''.join(line))

# 1초 ~ N-1초 수행
for second in range(1, n): 
    if second % 2 == 1:
        # 다음 초에 터뜨릴 폭탄 위치 찾아 저장
        bombs = finder(arr) 
        # 폭탄 채우기
        bombFill()
    else:
        # 폭탄 터뜨리기
        bang() 

printer(arr)