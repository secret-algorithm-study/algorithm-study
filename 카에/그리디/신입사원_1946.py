import sys
sys.stdin=open("input.txt", "r")

t = int(input())

for _ in range(t):
    n = int(input())
    scores = [tuple(map(int, input().split())) for _ in range(n)]
    scores.sort()

    target_score = scores[0][1]
    cnt = 1

    for i in range(1, n):
        if scores[i][1] < target_score:
            cnt+=1
            target_score = scores[i][1]

    print(cnt)



