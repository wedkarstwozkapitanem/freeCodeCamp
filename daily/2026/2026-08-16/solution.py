"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-16                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def are_anagrams(str1, str2):
    str1 = sorted("".join(i.lower() for i in str1 if not i.isspace()))
    str2 = sorted("".join(i.lower() for i in str2 if not i.isspace()))
    return str1 == str2