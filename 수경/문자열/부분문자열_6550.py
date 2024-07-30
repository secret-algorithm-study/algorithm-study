import sys
sys.stdin=open("input.txt", "r")

while True:
    try:
        s,t = map(list, input().split())
        
        for c in t:
            if s and s[0]==c: s.pop(0)
            
        print('No' if s else 'Yes')
    except: break