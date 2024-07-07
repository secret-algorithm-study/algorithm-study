def min_coin_count(N, K, coin_values):
    cnt = 0
    for i in range(N-1, -1, -1):
        if coin_values[i] <= K:
            cnt += K // coin_values[i]
            K %= coin_values[i]
    return cnt

N, K = map(int, input().split())
coin_values = [int(input()) for _ in range(N)]

print(min_coin_count(N, K, coin_values))

# 현재 동전의 가치가 K보다 작거나 같다면, 
# 해당 동전으로 만들 수 있는 최대 개수를 계산하여 카운트(cnt)에 더하기
# K를 해당 동전으로 나눈 나머지를 새로운 K로 업데이트
