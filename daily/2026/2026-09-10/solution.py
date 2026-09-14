"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-09-10                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def array_diff(arr1:list, arr2:list)->list:
    return sorted([i for i in arr1 if i not in arr2] + [i for i in arr2 if i not in arr1])