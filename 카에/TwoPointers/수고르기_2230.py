import sys
sys.stdin=open("input.txt", "r")

n, m = map(int, input().split())
nums = list((int(input()) for _ in range(n)))

nums.sort()

p1 = 0
p2 = 0
answer = sys.maxsize

while p1 < n and p2 < n:
    total = nums[p2]-nums[p1]

    if total >= m:
        answer = min(answer, total)
        p1+=1
    else:
        p2+=1
    
print(answer)
