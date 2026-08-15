"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-12                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def is_valid_number(n, base):
    try:
        int(n,base)
        return True
    except:
        return False

print(is_valid_number("10101", 2))
print(is_valid_number("10201", 2))
print(is_valid_number("76543210", 8))
print(is_valid_number("ABC", 20))