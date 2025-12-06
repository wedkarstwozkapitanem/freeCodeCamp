"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2025-12-04                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def silnia(a:int) -> int:
    wynik = int(1)
    while a:
        wynik *= a
        a -= 1
    return wynik

def count_permutations(s):
    s = s.lower()
    wynik = silnia(len(s)) #liczba wszystkich permutacji
    wystopienia = {}
    for i in s:
        if wystopienia.get(i):
            wystopienia[i] += 1
        else:
            wystopienia[i] = 1
    ##############################        
    # permutacje z powtórzeniami #
    #            n!              #
    # -------------------------- #
    #   n1! + n2! + n3! + ...    #
    #############################

    for i in wystopienia:
        wynik /= silnia(wystopienia[i])
    return wynik

print(count_permutations("abb"))