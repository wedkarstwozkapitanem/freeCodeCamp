"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-09-13                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def find_missing_numbers(arr:list) -> list:
    arr = sorted(arr)
    return [j for i in range(1,len(arr)) for j in range(arr[i - 1] + 1,arr[i])]

print(find_missing_numbers([1, 3, 5]))