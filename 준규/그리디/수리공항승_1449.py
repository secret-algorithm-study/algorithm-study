import sys
sys.stdin = open("/Users/jungyu/Documents/algorithm-study/준규/그리디/input.txt" , "r")


n , l = map(int, input().split());
holes = list(map(int, input().split()));


# 오름차순 정렬 된 구멍들
sortedHoles = sorted(holes);

# 시작 지점
start = sortedHoles[0];

# 총 tape 개수 (최소 1이상)
tape = 1;

for currentHole in sortedHoles[1:]:
    # 현재 위치 부터 다음 위치까지의 거리가 l 보다 크면 tape를 한개 사용
    if(currentHole - start >= l):
        tape += 1;
        start = currentHole;


print(tape);

