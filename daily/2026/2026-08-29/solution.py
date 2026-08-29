"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-29                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def burn_candles(candles:int, leftovers_needed:int) -> int:
    wynik = 0
    resztki = 0
    while(candles > 0):
        wynik += candles
        resztki += candles
        candles = resztki // leftovers_needed
        resztki %= leftovers_needed
          
    return wynik

print(burn_candles(7, 2))
print(burn_candles(20, 3))