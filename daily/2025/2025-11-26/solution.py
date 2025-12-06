"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2025-11-26                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def is_fizz_buzz(sequence):
    for i in range(1,len(sequence)+1):
        if i % 3 == 0 and i % 5 == 0:
            if sequence[i-1] != "FizzBuzz":
                return False
        elif i % 3 == 0:
            if sequence[i-1] != "Fizz":
                return False

        elif i % 5 == 0:
            if sequence[i-1] != "Buzz":
                return False
        elif sequence[i-1] != i:
            print(i,sequence[i-1])
            return False

    return True
