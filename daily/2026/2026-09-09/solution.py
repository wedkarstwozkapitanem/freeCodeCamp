"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-09-09                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""


def all_unique(s:str) -> str:
    znaki = set()
    for i in s:
        if i in znaki:
            return False
        znaki.add(i)
    return True

print(all_unique("abc"))