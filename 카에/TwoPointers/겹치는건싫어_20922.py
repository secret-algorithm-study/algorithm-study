import sys
sys.stdin=open("input.txt", "r")

n, k = map(int, input().split())
nums = list(map(int, input().split()))

p1 = 0
p2 = 1
max_cnt = 0

# 풀이 1 -> dictionary 사용

dic = {}
dic[nums[p1]] = 1

def check_duplicate(num):
    if not num in dic:
        return False
    elif dic[num] < k:
        return False
    else:
        return True

def add_dic(num):
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

def remove_dic(num):
    dic[num]-=1

while p2 < n:
    if check_duplicate(nums[p2]):
        remove_dic(nums[p1])
        p1 += 1
    else:
        add_dic(nums[p2])
        p2 += 1
        max_cnt = max(max_cnt, p2-p1)

print(max_cnt)

# 풀이 2 -> list 사용

checks = [0]*100001
checks[nums[p1]] = 1

while p2 < n:
    if checks[nums[p2]] < k:
        checks[nums[p2]] += 1
        p2 += 1
        max_cnt = max(max_cnt, p2-p1)   
    else:
        checks[nums[p1]] -= 1
        p1 += 1

print(max_cnt)
