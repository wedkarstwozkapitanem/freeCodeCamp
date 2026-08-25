"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-25                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""


def to_camel_case(s: str) -> str: 
    return "".join(
        slowo.lower() if i == 0 
        else slowo.lower().capitalize()  
        for i,slowo in enumerate(s.translate(str.maketrans({'-':' ','_' : ' '}))
        .split())
        )

print(to_camel_case("hello world"))
print(to_camel_case("secret agent-X"))