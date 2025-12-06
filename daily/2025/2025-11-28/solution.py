"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2025-11-28                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def compare(word, guess):
    mapa = {}
    wynik = ['0'] * len(word)
    for i in range(len(word)):
        if guess[i] == word[i]:
            wynik[i] = '2'
        elif mapa.get(word[i]):
            mapa[word[i]] += 1
        else:
            mapa[word[i]] = int(1)

    for i in range(len(guess)):
        if mapa.get(guess[i]):
            if mapa[guess[i]] > 0:
                wynik[i] = '1'
                mapa[guess[i]] -= 1
   
    
    return "".join(wynik)

print(compare("APPLE", "POPPA"))