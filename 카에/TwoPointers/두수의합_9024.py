import sys
sys.stdin=open("input.txt", "r")

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()

    p1 = 0
    p2 = n-1
    min_diff = sys.maxsize
    count = 0

    while p1 < p2:
        total = nums[p1]+nums[p2]
        diff = abs(k - total)
        if diff < min_diff:
            min_diff = diff
            count = 1
        elif diff == min_diff:
            count +=1

        if total > k:
            p2 -= 1
        else:
            p1 += 1
    print(count)



