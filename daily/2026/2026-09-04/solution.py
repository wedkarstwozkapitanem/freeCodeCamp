"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-09-04                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def repeat_vowels(s:str) -> str:
    slownik = {'a','e','i','o','u'}
    licznik = int(1)
    
    def powtorz(samogloska:str) -> str:
        nonlocal licznik
        tmp = ""
        if samogloska.lower() not in slownik:
            return samogloska
        tmp += samogloska
        for i in range(licznik - 1):
            tmp += samogloska.lower()
        licznik += 1
        return tmp

    return "".join(powtorz(i) for i in s)


print(repeat_vowels("hello world"))
print(repeat_vowels("freeCodeCamp"))
print(repeat_vowels("AEIOU"))