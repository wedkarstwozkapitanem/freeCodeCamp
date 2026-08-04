"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-04                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

import math

def calculate_handicap(scores, pars):
    return math.ceil(sum(i[0] - i[1] for i in zip(scores,pars)) / len(scores) * 10) / 10
    

print(calculate_handicap([72, 72, 72], [72, 72, 72]))
print(calculate_handicap([80, 76, 78, 78], [72, 72, 72, 72]))
print(calculate_handicap([42, 45, 46, 44], [36, 36, 36, 36]))