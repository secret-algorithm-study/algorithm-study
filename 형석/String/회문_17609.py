def yusa(S, p1, p2):
    while p1 < p2:
        if S[p1] == S[p2]:
            p1 += 1
            p2 -= 1
        else:
            return False
    return True
 
T = int(input())
 
for _ in range(T):
    S = input()
    p1, p2 = 0, len(S) - 1
    result = 0
    while p1 < p2:
        if S[p1] == S[p2]:
            p1 += 1
            p2 -= 1
        elif yusa(S, p1 + 1, p2) or yusa(S, p1, p2 - 1):
            result = 1
            break
        else:
            result = 2
            break
    print(result)
 