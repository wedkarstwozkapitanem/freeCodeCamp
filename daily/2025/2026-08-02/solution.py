"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2025-08-02                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def get_food_chain(pairs):
    mapa = {drapieznik : ofiara for drapieznik, ofiara in pairs}
    wszystkie_ofiary = { ofiara for drapieznik, ofiara in pairs}

    lancuch_pokarmowy = [next(drapieznik for drapieznik,_ in pairs if drapieznik not in wszystkie_ofiary)]

    while lancuch_pokarmowy[-1] in mapa:
        lancuch_pokarmowy.append(mapa[lancuch_pokarmowy[-1]])

    return lancuch_pokarmowy

print(get_food_chain([["seal", "salmon"], ["herring", "shrimp"], ["orca", "seal"], ["shrimp", "plankton"], ["salmon", "herring"]]))