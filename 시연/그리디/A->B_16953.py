def min_operations_to_transform(A, B):
    operations = 0

    while B > A:
        if B % 2 == 0:
            B //= 2
        elif B % 10 == 1:
            B //= 10
        else:
            return -1
        operations += 1

    if B == A:
        return operations + 1
    else:
        return -1

A, B = map(int, input().split())

print(min_operations_to_transform(A, B))

# 메모리 31120, 시간 40

def min_operations_to_transform(A, B):
    operations = 0

    while B > A:
        if B % 10 == 1:
            B //= 10
        elif B % 2 == 0:
            B //= 2
        else:
            return -1
        operations += 1

    if B == A:
        return operations + 1
    else:
        return -1

A, B = map(int, input().split())

print(min_operations_to_transform(A, B))

# 메모리 31120, 시간 40 

# 똑같음..?