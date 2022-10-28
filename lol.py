import random
n, m = map(int, [4, 5])
matrix = [[random.choice([0, 1]) for i in range(m)] for j in range(n)]
def printer(matrix):
    for elem in range(n):
        print(*matrix[elem])
printer(matrix)