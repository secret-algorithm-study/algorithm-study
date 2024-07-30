import sys
sys.stdin = open("input.text", "rt")
from collections import deque

while True:
    try:
        s,t = input().split()
        flag = 0
        idx = 0
        for i in range(len(t)):
            if t[i] == s[idx]:
                idx += 1
                if idx == len(s):
                    flag = 1
                    break
        if flag == 1:
            print("Yes")
        else:
            print("No")
    except:
        break

#### 따로 본 풀이 

import sys
from collections import deque

while True:
    try:
        s, t = input().split()
        queue = deque(list(s))

        for c in t:
            if queue and c == queue[0]:
                queue.popleft()

        if queue:
            print('No')
        else:
            print('Yes')
    except:
        break