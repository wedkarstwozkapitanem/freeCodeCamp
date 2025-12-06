"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2025-11-27                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def calculate_age(birthday):
    urudziny = list(map(int,birthday.split("-")))
    dzis = [2025,11,27]

    wiek = int(dzis[0] - urudziny[0])
    if urudziny[1] >= dzis[1]:
        if urudziny[1] == dzis[1] and urudziny[2] > dzis[2]:
            wiek -= 1
        elif urudziny[1] > dzis[1]:
            wiek -= 1

    return wiek

print(calculate_age("2006-05-02"))