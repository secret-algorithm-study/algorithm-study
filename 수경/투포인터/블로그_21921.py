# 연속부분합
import sys
sys.stdin=open("input.txt", "r")

n,x = map(int,input().split())
v = list(map(int,input().split()))

s,e = 0,x-1
sum_v = sum(v[s:e+1])
max_v = sum_v
max_v_cnt = 1

while e < n-1:
    sum_v -= v[s]
    
    s += 1
    e += 1
    
    sum_v += v[e]
    
    if sum_v > max_v: # 초과
        max_v = sum_v
        max_v_cnt = 1
    elif sum_v < max_v: # 미만
        continue
    else: # 동일
        max_v_cnt += 1

if max_v == 0:
    print('SAD')
else:
    print(max_v, max_v_cnt, sep='\n')
