"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-13                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""


def fibonacci_sequence(start_sequence, length):
    if length == 0:
        return []
    if length == 1:
        return [start_sequence[0]]

    ciog_fib = start_sequence
    for i in range(2,length):
        ciog_fib.append(ciog_fib[i-2] + ciog_fib[i-1])
    return ciog_fib

print(fibonacci_sequence([0, 1], 20))
print(fibonacci_sequence([21, 32], 1))
print(fibonacci_sequence([0, 1], 0))
print(fibonacci_sequence([10, 20], 2))
print(fibonacci_sequence([123456789, 987654321], 5))