"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-05                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""


def get_spoken_duration(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    wynik = list()

    if hours:
        wynik.append(f'{hours} {"hours" if hours != 1 else "hour"}')
    
    if minutes:
        wynik.append(f'{minutes} {"minutes" if minutes != 1 else "minute"}')

    if seconds:
        wynik.append(f'{seconds} {"seconds" if seconds != 1  else "second"}')
    if not wynik:
        return "0 seconds"
    elif len(wynik) == 1:
        return wynik[0]
    elif len(wynik) == 2:
        return " and ".join(wynik)

    return wynik[0] + ", " + wynik[1] + " and " + wynik[2]
   
    

print(get_spoken_duration(3723))
print(get_spoken_duration(7295))
print(get_spoken_duration(435))
print(get_spoken_duration(14455))
print(get_spoken_duration(72000))