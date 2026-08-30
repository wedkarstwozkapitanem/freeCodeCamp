"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-30                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def find_duplicates(arr:list) -> list:
    arr = sorted(arr)
    wynik = list()
    for i in range(1,len(arr)):
        if(arr[i] == arr[i-1]):
            if len(wynik) == 0:
                wynik.append(arr[i])
            elif wynik[-1] != arr[i]:
                wynik.append(arr[i])

    return wynik

print(find_duplicates([1, 2, 3, 4, 1, 2]))