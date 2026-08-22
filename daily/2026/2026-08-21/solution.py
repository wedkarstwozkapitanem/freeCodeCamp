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
    ilosc_minut = (int(duration[0]) * 60 + int(duration[1])) / float(miles)
    ilosc_godzin =  math.floor(float(ilosc_minut) / 60)
    ilosc_minut = int(ilosc_minut % 60)
    return f"{ilosc_godzin:02d}:{ilosc_minut:02d}"

print(mile_pace(3, "24:00"))
print(mile_pace(2, "07:00"))
print(mile_pace(26.2, "120:35"))