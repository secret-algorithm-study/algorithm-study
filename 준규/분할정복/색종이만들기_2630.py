
import sys

sys.stdin = open('input.txt', 'r')

n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]


white = 0;
blue = 0;


def divider(x , y , n):
    global white, blue

    color = paper[x][y];

    for i in range(x , x + n):
        for j in range(y , y + n):
            if paper[i][j] != color:
                divider(x , y , n // 2)
                divider(x, y + n // 2, n // 2)
                divider(x + n // 2, y, n // 2)
                divider(x + n // 2, y + n // 2, n // 2)
                return
            
    if color == 0:
        white += 1
    else:
        blue += 1

divider(0, 0, n)

print(white)
print(blue)

