"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-09-03                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def is_pangram(sentence:str, letters:str) -> bool:
    slownik = dict(map(lambda x: (x,1),letters.lower()))
    for i in sentence.lower():
        if not i.isalpha():
            continue
        if i in slownik:
            slownik[i] = 0
        else:
            return False

    return not any(True for i in slownik if slownik[i] == 1)

print(is_pangram("hello", "helo"))
print(is_pangram("hello", "helow"))