import sys
sys.stdin = open('input.txt', 'r')

result = 0

n, m = map(int, input().split())

preferences = [list(map(int, input().split())) for _ in range(n)]

for i in range(m):
    for j in range(i+1, m):
        for k in range(j+1, m):
            satisfact = 0

            for preference in preferences:
                satisfact += max(preference[i], preference[j], preference[k])

            result = max(result, satisfact)

print(result)