import sys
sys.stdin=open("input.txt", "r")

s = input()

target_num = ''
zero_cnt = 0
one_cnt = 0

for i in range(0, len(s)):
    if s[i] == '0' and target_num != '0':
        zero_cnt += 1
        target_num = '0'
    elif s[i] == '1' and target_num != '1':
        one_cnt +=1
        target_num = '1'

print(min(zero_cnt, one_cnt))