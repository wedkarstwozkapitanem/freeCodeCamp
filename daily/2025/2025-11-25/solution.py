"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2025-11-24                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def fizz_buzz(n):
    wynik = list()
    for i in range(1,n+1):
        if i%3 == 0 and i%5 == 0:
            wynik.append("FizzBuzz")
        elif i%3 == 0:
            wynik.append("Fizz")
        elif i%5 == 0:
            wynik.append("Buzz")
        else:
            wynik.append(i)
    return wynik
print(fizz_buzz(8))
