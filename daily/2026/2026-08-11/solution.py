"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-11                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def is_balanced(s):
    samogloski = {"a","e","i","o","u"}

    return sum(i in samogloski for i in s[:len(s) // 2].lower()) == sum( i in samogloski for i in s[(len(s) + 1) // 2:].lower())

print(is_balanced("Kitty Ipsum"))
print(is_balanced("racecar"))
print(is_balanced("Lorem Ipsum"))
print(is_balanced("string"))
print(is_balanced(" "))