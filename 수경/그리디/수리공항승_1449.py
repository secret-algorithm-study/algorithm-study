n, l = map(int, input().split())
breaks = sorted(map(int, input().split()))

last_covered = 0
tape_count = 0

for b in breaks:
    if b > last_covered:
        last_covered = b + l - 1
        tape_count += 1

print(tape_count)
