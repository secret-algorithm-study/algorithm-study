M, N = map(int, input().split())

matrix = [[1 if char == 'X' else 0 for char in input()] for _ in range(M)]

result = 0

for i in range(len(matrix)):
	top, bottom = int(10e8), int(10e8)
	for j in range(len(matrix[0])):
		if matrix[i][j]: continue
		if i - 1 >= 0 and matrix[i - 1][j] == 1:
			if j - top == 1:
				top = int(10e8)
				result += 1
			else:
				top = j
		if i + 1 < len(matrix) and matrix[i + 1][j] == 1:
			if j - bottom == 1:
				bottom = int(10e8)
				result += 1
			else:
				bottom = j

for j in range(len(matrix[0])):
	left, right = int(10e8), int(10e8)
	for i in range(len(matrix)):
		if matrix[i][j]: continue
		if j - 1 >= 0 and matrix[i][j - 1] == 1:
			if i - left == 1:
				left = int(10e8)
				result += 1
			else:
				left = i
		if j + 1 < len(matrix[0]) and matrix[i][j + 1] == 1:
			if i - right == 1:
				right = int(10e8)
				result += 1
			else:
				right = i

print(result)