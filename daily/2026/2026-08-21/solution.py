"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-21                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

import math
def mile_pace(miles, duration):
    duration = duration.split(":")
    ilosc_minut = (float(duration[0]) * 60 + float(duration[1])) / float(miles)
    ilosc_godzin =  str(math.floor(float(ilosc_minut) / 60)) 
    ilosc_minut = str(int(ilosc_minut % 60))
    return ilosc_godzin if len(ilosc_godzin) == 2 else "0" + ilosc_godzin + ":" +  (ilosc_minut if len(ilosc_minut) == 2 else "0" +  ilosc_minut)

print(mile_pace(3, "24:00"))
print(mile_pace(2, "07:00"))
print(mile_pace(26.2, "120:35"))