import sys
sys.stdin = open('input.txt', 'r')


n, k = map(int, input().split())  
dolls = list(map(int, input().split()))  

left = 0  
ryan_count = 0  
min_length = float('inf')


for right in range(n):
    # 현재 인형이 라이언이면 카운트 증가
    if dolls[right] == 1:
        ryan_count += 1
    
    # 라이언 인형이 k개 이상이면 최소 길이 갱신 시도
    while ryan_count >= k:
        # 현재 부분 배열의 길이와 기존 최소 길이 중 작은 값으로 갱신
        min_length = min(min_length, right - left + 1)
        # 왼쪽 포인터를 오른쪽으로 이동하며 불필요한 인형 제거
        if dolls[left] == 1:
            ryan_count -= 1
        left += 1

# 결과 출력: 조건을 만족하는 부분 배열이 있으면 그 길이를, 없으면 -1 출력
print(min_length if min_length != float('inf') else -1)