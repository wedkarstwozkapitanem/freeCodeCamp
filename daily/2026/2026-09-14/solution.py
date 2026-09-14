"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-09-14                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def get_words(paragraph:str)->list:
    liczba_slow = dict()

    paragraph = paragraph.translate(str.maketrans("","",",.!")).lower().split(" ")
    for i in paragraph:
        if i in liczba_slow:
            liczba_slow[i] += 1
        else:
            liczba_slow.update({i:1})

    return list(i[0] for i in sorted(liczba_slow.items(),key = lambda x:x[1],reverse=True))[:3]

print( get_words("abc.,!"))
print(get_words("Coding in Python is fun because coding Python allows for coding in Python easily while coding"))