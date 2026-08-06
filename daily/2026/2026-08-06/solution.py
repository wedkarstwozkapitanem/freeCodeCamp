"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-06                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def get_spoken_time(hour_angle, minute_angle):
    hour = int((hour_angle // 30) % 12) 
    minutes = (minute_angle // 6) % 60
    if hour == 0:
        hour = 12

    if minutes == 0:
        return f"{hour} o'clock"
    elif minutes == 15:
        return f"quarter past {hour}"
    elif minutes >= 1 and minutes <= 29:
        return f"{minutes} minutes past {hour}"
    elif minutes == 30:
        return f"half past {hour}"
    elif minutes == 45:
        return f"quarter to {hour + 1 if hour != 12 else 1}"

    return f"{60 - minutes} minutes to {hour + 1 if hour != 12 else 1}"

print(get_spoken_time(90, 0))
print(get_spoken_time(160, 120))
print(get_spoken_time(255, 180))
print(get_spoken_time(67.5, 92))