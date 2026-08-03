"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-03                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def get_emoji_phrase(s):
    slownik = {
        "👶":"baby",
        "🐱":"cat",
        "🐕":"dog",
        "🐟":"fish",
        "🥵":"hot",
        "🧊":"ice",
        "🪨":"rock",
        "🦈":"shark",
        "🍲":"soup",
        "⭐":"star"
    }

    wynik = str()
    for i in s:
        wynik += slownik[i] + " "
    return wynik[:-1]

print(get_emoji_phrase("⭐🐟"))