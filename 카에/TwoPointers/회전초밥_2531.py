import sys
sys.stdin=open("input.txt", "r")

n, d, k, c = map(int, input().split())
belt = list(int(input()) for _ in range(n))

max_sushi = 0

for i in range(n):
    eat_cnt = 1
    checks = [0]*(d+1)
    checks[c] = 1

    for j in range(i, i+k):
        sushi = belt[j%n]

        if checks[sushi] == 0:
            eat_cnt += 1
        checks[sushi] += 1
    max_sushi = max(max_sushi, eat_cnt)

print(max_sushi)




