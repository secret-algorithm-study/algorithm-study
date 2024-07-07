import sys
sys.stdin=open("input.txt", "r")

n = int(input())
nums = list(map(int, input().split()))

increase = [1]*100001
decrease = [1]*100001

for i in range(1, n):
    if nums[i-1] <= nums[i]:
        increase[i] = increase[i-1]+1
    if nums[i-1] >= nums[i]:
      decrease[i] = decrease[i-1]+1
    
print(max(max(increase), max(decrease)))