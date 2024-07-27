import sys
sys.stdin=open("input.txt", "r")

while True:
    try:
        s, t = input().split()

        p1 = 0
        p2 = 0
        answer = ''
    
        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                answer += t[p2]
                p1 += 1
                p2 += 1
            else:
                p2 += 1
    
        if s == answer:
            print('Yes')
        else:
            print('No')    
    except:
        break