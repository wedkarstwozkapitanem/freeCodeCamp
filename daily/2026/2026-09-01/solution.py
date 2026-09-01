"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-09-01                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def tribonacci_sequence(start_sequence:int, length:int)->list:
    if length <= 3:
        return start_sequence[0:length]
    
    for i in range(length - 3):
        start_sequence.append(start_sequence[i] + start_sequence[i + 1] + start_sequence[i + 2])

    return start_sequence
    

print(tribonacci_sequence([0, 0, 1], 20))