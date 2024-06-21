import sys
sys.stdin=open("input.txt", "r")

n, m = map(int, input().split())

if n == 0:
    print(0)
    exit()

books = list(map(int, input().split()))

cur_weight = 0;
box_cnt = 1

for book in books:
    if cur_weight + book <= m:
        cur_weight += book
    else:
        cur_weight = book
        box_cnt += 1

print(box_cnt)