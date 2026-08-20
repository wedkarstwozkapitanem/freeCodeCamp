"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-20                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def squares_with_three(n):

    return sum(1 for i in range(n + 1) if str(i * i).find('3') != -1)

print(squares_with_three(10))
print(squares_with_three(100))
print(squares_with_three(1000))
