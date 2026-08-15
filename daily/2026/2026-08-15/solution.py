"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-12                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def jbelmu(text):
    return " ".join(i if len(i) == 1 else i[0] + "".join(sorted(i[1:-1])) + i[-1] for i in text.split())

print(jbelmu("hello world"))
print(jbelmu("i love jumbled text"))