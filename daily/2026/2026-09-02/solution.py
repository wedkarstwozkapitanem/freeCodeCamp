"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-09-02                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def rgb_to_hex(rgb: str) -> str:
    rgb = [hex(int(i))[2:]  for i in rgb[4:-1].split(', ')]
    return "#" + "".join(i if len(i) == 2 else "0" + i for i in rgb)

print(rgb_to_hex("rgb(255, 255, 255)"))
print(rgb_to_hex("rgb(1, 11, 111)"))