"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-24                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""


def battle(my_army, opposing_army):
    if(len(my_army) > len(opposing_army)):
        return "Opponent retreated"
    elif(len(my_army) < len(opposing_army)):
        return "We retreated"

    def zamien_na_liczbe(zolniez: str) -> int:
        if zolniez[0] >= '0' and zolniez[0] <= '9':
            return int(zolniez[0])
        elif zolniez[0] >= 'a' and zolniez[0] <= 'z':
            return ord(zolniez[0]) - ord('a')
        elif zolniez[0] >= 'A' and zolniez[0] <= 'Z':
            return ord(zolniez[0]) - ord('A') + 27
        return int(0)
    
    liczba_moich_zwyciestw = int(0)
    liczba_przegranych = int(0)

    for moj_zolniez,przeciwnika_zolniez in zip(my_army,opposing_army):
        moja_sila = zamien_na_liczbe(moj_zolniez)
        przeciwnika_sila = zamien_na_liczbe(przeciwnika_zolniez)
        if(moja_sila > przeciwnika_sila):
            liczba_moich_zwyciestw += 1
        elif(moja_sila < przeciwnika_sila):
            liczba_przegranych += 1

    if(liczba_moich_zwyciestw > liczba_przegranych):
        return "We won"
    elif (liczba_moich_zwyciestw < liczba_przegranych):
        return "We lost"
    return "It was a tie"

print(battle("Hello", "World"))
print(battle("pizza", "salad"))