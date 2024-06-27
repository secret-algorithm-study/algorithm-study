def min_tapes_to_fix_leaks(N, L, leak_positions):
    leak_positions.sort()
    tape_count = 0
    current_end = 0

    for leak in leak_positions:
        if current_end < leak:
            tape_count += 1
            current_end = leak + L - 1
    
    return tape_count

input_data = input().split()
N = int(input_data[0])
L = int(input_data[1])
leak_positions = list(map(int, input().split()))

print(min_tapes_to_fix_leaks(N, L, leak_positions))