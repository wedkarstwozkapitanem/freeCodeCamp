"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-23                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

import math

def is_unnatural_prime(n):
    n = abs(n)
    if n in [0,1]:
         return False
    return not any(True for i in range(2,int(math.sqrt(n)) + 1) if n % i == 0)

print(is_unnatural_prime(-1))
print(is_unnatural_prime(99))