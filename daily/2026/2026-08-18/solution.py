"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-18                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def factorial(n):
    n = int(n)
    if n <= 1:
        return 1
    wynik = 1
    while n > 1:
        wynik *= n
        n -= 1
    return wynik

print( factorial(5))