import sys
sys.stdin=open("input.txt", "r")

n = int(input())
items = [int(input()) for _ in range(n)]
items.sort(reverse=True)

price = 0

for i in range(0, n, 3):
    item = items[i:i+3]

    if len(item) == 1:
        price += item[0]
    else:
        price += item[0] + item[1]

print(price)