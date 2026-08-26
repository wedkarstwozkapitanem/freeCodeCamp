"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-26                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def decode(s: str) -> str:

    dekoder = [""]
    for i in s:
        if i == "(":
            dekoder.append("")
        elif i == ")":
            ostatni = dekoder.pop()[::-1]
            dekoder[-1] += ostatni
        else:
            dekoder[-1] += i
    return dekoder[0]
    
print(decode("(f(b(dc)e)a)"))
print(decode("((is?)(a(t d)h)e(n y( uo)r)aC)"))
print(decode("f(Ce(re))o((e(aC)m)d)p"))