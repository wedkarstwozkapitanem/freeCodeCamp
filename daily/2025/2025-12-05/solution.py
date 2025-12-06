"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2025-12-05                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def difference(arr1, arr2):
    wynik = list()
    for i in arr1:
        if not(i in arr2):
            wynik.append(i)

    for i in arr2:
        if not(i in arr1):
            wynik.append(i)         
    return wynik