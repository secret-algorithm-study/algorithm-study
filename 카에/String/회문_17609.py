import sys
sys.stdin=open("input.txt", "r")

t = int(input())

# 유사회문인지 확인하는 함수
def is_pseudo_palindrome(word, p1, p2):
    while p1 < p2:
        if word[p1] != word[p2]:
            return False
        else:
            p1+=1
            p2-=1
    return True

for _ in range(t):
    word = input()
    p1 = 0
    p2 = len(word)-1
    answer = 0

    while p1 < p2:
        if word[p1] == word[p2]:
            p1 += 1
            p2 -= 1
        else:
            # 한 문자를 삭제하고 비교
            if(is_pseudo_palindrome(word, p1+1, p2) or is_pseudo_palindrome(word, p1, p2-1)):
                answer = 1
                break
            else:
                answer = 2
                break
    
    print(answer)