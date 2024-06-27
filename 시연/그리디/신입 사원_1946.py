import sys
input = sys.stdin.readline

def max_hireable_candidates(test_cases):
    results = []
    
    for case in test_cases:
        n, candidates = case
        candidates.sort()
        
        max_candidates = 1
        best_interview_rank = candidates[0][1]
        
        for i in range(1, n):
            if candidates[i][1] < best_interview_rank:
                max_candidates += 1
                best_interview_rank = candidates[i][1]
        
        results.append(max_candidates)
    
    return results

t = int(input().strip())
test_cases = []

for _ in range(t):
    n = int(input().strip())
    candidates = [tuple(map(int, input().strip().split())) for _ in range(n)]
    
    #for _ in range(n):  이 반복문과 같음 
        #doc_rank, int_rank = map(int, input().strip().split())
        #candidates.append((doc_rank, int_rank))

    test_cases.append((n, candidates))

results = max_hireable_candidates(test_cases)
for result in results:
    print(result)
