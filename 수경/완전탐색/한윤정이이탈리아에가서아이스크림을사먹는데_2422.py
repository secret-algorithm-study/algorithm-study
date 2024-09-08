import sys
sys.stdin=open("input.txt", "r")

n, m = map(int, input().split())
avoid = set(tuple(sorted(map(int, input().split()))) for _ in range(m))

count = 0

for a in range(1, n-1):
    for b in range(a+1, n):
        for c in range(b+1, n+1):
            if (a, b) in avoid or (b, c) in avoid or (a, c) in avoid: continue
            count += 1

print(count)
