import sys
sys.stdin = open('input.txt', 'r')


n, k =  map(int, input().split())
inputs = [list(map(int, input().split())) for _ in range(n)]

cage = [0 for _ in range(1000001)]

for i in range(n):
    cage[inputs[i][1]] = inputs[i][0]


bearRange = 2*k + 1


initSum = sum(cage[:bearRange])
result = initSum

for i in range(bearRange , 1000001):
    initSum += cage[i] - cage[i - bearRange]

    if (result < initSum):
        result = initSum


print(result)