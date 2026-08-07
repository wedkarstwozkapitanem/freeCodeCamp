"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-07                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def is_valid_nonogram(clue, cells):
    idx = 0
    for blok in clue:
        while idx < len(cells) and cells[idx] == 0:
            idx += 1

        for _ in range(blok):
            if idx >= len(cells) or cells[idx] == 0:
                return False
            idx += 1
        if idx < len(cells) and cells[idx] == 1:
            return False

    while idx < len(cells):
        if cells[idx] == 1:
            return False
        idx += 1
    return True

print(is_valid_nonogram([3, 2], [1, 1, 1, 0, 1, 1]))
print(is_valid_nonogram([3, 2], [0, 1, 1, 1, 1, 1]))
print(is_valid_nonogram([1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1]))