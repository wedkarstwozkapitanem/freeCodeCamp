"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-09-07                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def parse_roman_numeral(numeral:str) -> int:
    ostatnie = int(0)
    slownik = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }

    wynik = int(0)

    for i,litera in enumerate(numeral):
        if( i < len(numeral) - 1 and slownik[litera] < slownik[numeral[i+1]]) :
            wynik -= slownik[litera]
        else:
            wynik += slownik[litera]
        
        ostatnia = litera 

    return wynik

print(parse_roman_numeral("III"))
print(parse_roman_numeral("IV"))
print(parse_roman_numeral("XXVI"))
print(parse_roman_numeral("XCIX"))
print(parse_roman_numeral("CDLX"))