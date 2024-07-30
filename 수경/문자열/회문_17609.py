import sys
sys.stdin=open("input.txt", "r")

t = int(input())
targets = [input() for _ in range(t)]
ans_list = []

# 검사 중 회문이 아님을 확인 시, 검사 시점의 (f,b) idx 반환
def check_is_not_palindrome(str):
    chars = list(str)
    for i in range(len(chars)//2):
        f = i
        b = -i-1
        
        if (f==b): break
        if (chars[f]!=chars[b]): return (f,b)
    return 0

for target in targets:
    is_not_palindrome = check_is_not_palindrome(target)
    
    # is palindrome
    if not is_not_palindrome:
        ans_list.append(0)
        continue

    f,b = is_not_palindrome
    without_f = list(target)
    without_b = list(target)
    
    without_f.pop(f)
    without_b.pop(b)
    
    # not even almost palindrom
    if check_is_not_palindrome(without_f) and check_is_not_palindrome(without_b): ans_list.append(2)
    
    # almost palindrome
    else: ans_list.append(1)
    
for ans in ans_list: print(ans)