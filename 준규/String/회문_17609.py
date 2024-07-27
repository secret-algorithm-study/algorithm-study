import sys
sys.stdin = open('input.txt', 'r')

def check_pseudo_palindrome(s):
    
    left = 0
    right = len(s) - 1

    while left < right:
        # 양쪽 문자가 같은 경우
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            # 왼쪽 문자를 제거한 경우 확인
            left_removed = True
            l, r = left + 1, right
            while l < r:
                if s[l] != s[r]:
                    left_removed = False
                    break
                l += 1
                r -= 1
            
            if left_removed:
                return 1
            
            # 오른쪽 문자를 제거한 경우 확인
            right_removed = True
            l, r = left, right - 1
            while l < r:
                if s[l] != s[r]:
                    right_removed = False
                    break
                l += 1
                r -= 1
            
            if right_removed:
                return 1
            
            # 둘 다 아니면 회문 X
            return 2

    # while 루프를 빠져나왔다면 회문
    return 0


T = int(input())
for _ in range(T):
    s = input().strip()
    result = check_pseudo_palindrome(s)
    
    # 결과 출력
    if result == 0:
        print(0)
    elif result == 1:
        print(1)
    else:
        print(2)

  