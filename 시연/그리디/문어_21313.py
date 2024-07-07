n = int(input())

res = []
for i in range(n):
    if i == n - 1 and n % 2 != 0:
        res.append('3')
    else:
        res.append(str(i % 2 + 1))

print(" ".join(res))
