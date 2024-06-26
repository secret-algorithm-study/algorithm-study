import sys
input = sys.stdin.read

def count_non_overlapping_meetings(data):
    N = int(data[0])
    
    meetings = []
    for i in range(N):
        start, end = int(data[2 * i + 1]), int(data[2 * i + 2])
        meetings.append((start, end))
    
    meetings.sort(key=lambda x: (x[1], x[0]))
    
    count = 0
    last_end_time = 0
    
    for start, end in meetings:
        if start >= last_end_time:
            last_end_time = end
            count += 1
    
    return count

data = input().split()
result = count_non_overlapping_meetings(data)
print(result)
