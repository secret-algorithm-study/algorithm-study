import sys
sys.stdin=open("input.txt", "r")

n = int(input())
drinks = list(map(int, input().split()))
drinks.sort()

p1 = 0

while p1 < n-1:
    drinks[-1] = drinks[p1] / 2 + drinks[-1]
    p1+=1

print(drinks[-1])