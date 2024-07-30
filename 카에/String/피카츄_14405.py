import sys
sys.stdin=open("input.txt", "r")

s = input()

idx = 0
n = len(s)

while idx < n:
    if s[idx:idx+2] == 'pi':
        idx += 2
    elif s[idx:idx+2] == 'ka':
        idx += 2
    elif s[idx:idx+3] == 'chu':
        idx += 3
    else:
        print('NO')
        break
else:
    print('YES')