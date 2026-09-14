"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-09-08                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def build_acronym(s:str) -> str:
    nie_dozwolone = {"a","for","an","and","by","of"}
    return "".join(i[0].upper() for i in s.split(" ") if i not in nie_dozwolone)


print(build_acronym("National Aeronautics and Space Administration"))