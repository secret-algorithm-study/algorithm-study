def arithmetic(n):
    shakes = [1, 2] * (n // 2)
    if n % 2 != 0:
        shakes += [3]
    print(*shakes)  


def greedy(n):
    hands = list(range(1, 9))
    handsPool = [hands[:] for _ in range(n)]
    shakes = []

    for i in range(n):
        curOct = handsPool[i]
        nextOct = handsPool[i + 1 if i + 1 <= n - 1 else 0]
        shake = -1

        for hand in hands:
            if hand not in curOct:
                continue
            if hand not in nextOct:
                continue
            shake = hand
            break

        curOct.remove(shake)
        nextOct.remove(shake)

        shakes.append(shake)

    print(*shakes)


n = int(input())
arithmetic(n)
