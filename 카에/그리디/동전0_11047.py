import sys
sys.stdin=open("input.txt", "r")

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

coins.sort(reverse=True)

coin_count = 0

for coin in coins:
    if k > coin:
        coin_count += k // coin
        k %= coin

print(coin_count)