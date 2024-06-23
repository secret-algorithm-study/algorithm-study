def greedy(change):
    coins = 0
    remain = change

    while (remain > 0):
        if remain % 5 == 0:
            coins += remain // 5
            remain = 0
            break

        remain -= 2
        coins += 1

    print(coins) if remain == 0 else print(-1)


change = int(input())
greedy(change)
