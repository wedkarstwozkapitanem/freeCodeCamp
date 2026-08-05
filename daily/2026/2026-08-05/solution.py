"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-05                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""


import math

def get_spoken_duration(seconds):
    hour = math.floor(seconds / 3600)
    minuts = math.floor((seconds - (hour * 3600)) / 60)
    seconds = seconds - (hour * 3600) - (minuts * 60)
    h = "hours" if hour != 1 else "hour"
    m = "minutes" if minuts != 1 else "minute"
    s = "seconds" if seconds != 1  else "second"

    return (str(hour) + " " + h + (", " if minuts and seconds else "") if hour > 0 else "") + (str(minuts) + " " + m if minuts > 0 else "") + (" and " if (hour and seconds) or (minuts and seconds) or (hour and minuts) else "") + ((str(seconds) + " " + s) if seconds > 0 or (hour == 0 and minuts == 0) else "")
   
    return  h +  + str(minuts) + " " + m + " and " + str(seconds) + " " + s  

print(get_spoken_duration(3723))
print(get_spoken_duration(7295))
print(get_spoken_duration(435))
print(get_spoken_duration(14455))
print(get_spoken_duration(72000))