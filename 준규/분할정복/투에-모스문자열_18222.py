import sys

sys.stdin = open('input.txt', 'r')

k = int(input()) - 1


def helper(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2 == 0:
        return helper(n // 2)
    else:
        return 1 - helper(n // 2)

print(helper(k))