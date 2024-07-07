import sys
sys.stdin=open("input.txt", "r")

formula = input().split('-')
nums = []

for i in formula:
    if i.isdigit():
        nums.append(int(i))
    else:
        tmp = list(map(int, i.split('+')))
        nums.append(sum(tmp))

result = nums[0]

for i in range(1, len(nums)):
    result -= nums[i]

print(result)