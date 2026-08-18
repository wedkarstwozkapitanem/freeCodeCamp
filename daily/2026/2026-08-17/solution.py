"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-17                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def szukaj_indeks(arr, szukany, lewy = 0):
    for i in range(lewy,len(arr)):
        if arr[i] == szukany:
            return i
    return None

def find_target(arr, target):
    for i in range(len(arr)):
        idx = szukaj_indeks(arr,(target - arr[i]),i + 1)
        if idx:
            return [i,idx]
    return "Target not found"

print(find_target([2, 7, 11, 15], 9))
print(find_target([3, 2, 4, 5], 6))