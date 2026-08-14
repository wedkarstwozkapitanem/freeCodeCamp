"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-14                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def space_jam(s):

    return "  ".join(i.upper() for i in s if i != " ")

print(space_jam("freeCodeCamp"))