import sys
from itertools import combinations
sys.stdin = open('input.txt', 'r')

h , w = map(int, input().split());

n = int(input())


stickers = []

maximum = 0

for _ in range(n):
    stickers.append(list(map(int, input().split())))



for comb in combinations(stickers, 2):
    

    sticker1 = comb[0]
    sticker2 = comb[1]


    r1 = sticker1[0]
    c1 = sticker1[1]

    r2 = sticker2[0]
    c2 = sticker2[1]

    area1 = r1 * c1
    area2 = r2 * c2


    # 상하로 나란히 붙일때
    if((r1 + r2 <= h and max(c1, c2) <= w) or (max(r1, r2) <= h and c1+c2 <= w)):
        maximum = max(maximum , area1 + area2 )
    # 하나를 90도
    if (c1 + r2 <= h and max(r1, c2) <= w) or (max(c1, r2) <= h and r1 + c2 <= w):
        maximum = max(maximum , area1 + area2 )
    # 나머지 하나를 90도
    if (r1 + c2 <= h and max(c1, r2) <= w) or (max(r1, c2) <= h and c1 + r2 <= w):
        maximum = max(maximum , area1 + area2 )
    # 둘다 90도
    if (c1 + c2 <= h and max(r1, r2) <= w) or (max(c1, c2) <= h and r1 + r2 <= w):
        maximum = max(maximum , area1 + area2 )



print(maximum)