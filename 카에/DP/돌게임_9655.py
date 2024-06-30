import sys
sys.stdin=open("input.txt", "r")

n = int(input())

# 풀이 1
# print('CY' if n % 2 == 0 else 'SK')


# 풀이 2 (DP)
dy = [0]*1001
dy[1] = 'SK'
dy[2] = 'CY'
dy[3] = 'SK'

for i in range(4, n+1):
    if dy[i-1] == 'SK' or dy[i-3] == 'SK':
        dy[i] = 'CY'
    else:
        dy[i] = 'SK'

print(dy[n])

