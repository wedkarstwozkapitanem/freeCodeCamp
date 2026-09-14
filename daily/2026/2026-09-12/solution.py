"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-09-12                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def too_much_screen_time(hours:int) -> bool:

    return any(i >= 10 for i in hours) or any((sum(hours[i:i+3]) / 3) >= 8 for i in range(len(hours)-2)) or (sum(hours) / len(hours) >= 6)

print(too_much_screen_time([1, 2, 3, 4, 5, 6, 7]))