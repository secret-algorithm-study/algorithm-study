import sys
sys.stdin=open("input.txt", "r")

n, k = map(int, input().split())
nums = list(map(int, input().split()))

p1 = 0
delete_cnt = 0
answer = 0

for p2 in range(n):
    if nums[p2] % 2 == 1:
        delete_cnt += 1
    
    while delete_cnt > k:
        if nums[p1] % 2 == 1:
            delete_cnt -=1
        p1 += 1
    
    answer = max(answer, p2-p1+1-delete_cnt)

print(answer)
