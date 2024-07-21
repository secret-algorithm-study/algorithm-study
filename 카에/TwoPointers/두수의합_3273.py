import sys
sys.stdin=open("input.txt", "r")

n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()

p1 = 0
p2 = n-1
cnt = 0

while p1 < p2:
    total = nums[p1] + nums[p2]
    if total == x:
        cnt += 1
        p1 += 1
        p2 -= 1
    elif total < x:
        p1 += 1
    else:
        p2 -=1

print(cnt)
