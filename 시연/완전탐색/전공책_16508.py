from itertools import combinations

def min_cost_to_form_word(target, books):
    n = len(books)
    min_cost = float('inf')
    
    target_counts = {}
    for char in target:
        target_counts[char] = target_counts.get(char, 0) + 1
    
    for r in range(1, n + 1):
        for combo in combinations(books, r):
            combined_counts = {}
            combined_cost = 0
            
            for cost, title in combo:
                combined_cost += cost
                for char in title:
                    combined_counts[char] = combined_counts.get(char, 0) + 1
            
            # 현재 조합으로 목표 단어를 만들 수 있는지 확인
            if all(combined_counts.get(char, 0) >= 
            target_counts[char] for char in target_counts):
                min_cost = min(min_cost, combined_cost)
    
    return min_cost if min_cost != float('inf') else -1

T = input().strip()
N = int(input().strip())
books = []

for _ in range(N):
    C, W = input().strip().split()
    books.append((int(C), W))

result = min_cost_to_form_word(T, books)
print(result)
