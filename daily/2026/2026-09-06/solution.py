"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-09-06                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def rotate(matrix:list) -> list:
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(i+1,m):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        matrix[i].reverse()

    return matrix


for i in rotate([[1,2],[3,4]]):
    print(i)

print()

for i in rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]):
    print(i)