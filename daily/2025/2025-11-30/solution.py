"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2025-11-30                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def detect_ai(text):
    if(text.count('-') >= 2):
        return "AI"
    if(text.count('(') >= 2 and text.count(')') >= 2):
        return "AI"
    
    podzial = list(text.split())

    liczbaslowwiekszychliter = [len(i) for i in podzial]
    liczbaslow = int(0)
    for i in liczbaslowwiekszychliter:
        if i >= 7:
            liczbaslow += 1
        if liczbaslow >= 2:
            return "AI"

    import re

    return "Human"

print(detect_ai("The quick brown fox jumped over the lazy dog."))