"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-09-05                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""


def is_valid_ipv4(ipv4:str) -> bool:
    ipv4 = ipv4.split('.')
    return len(ipv4) == 4 and all(i.isnumeric() and int(i) <= 255 and not (i[0] == '0' and len(i) > 1) for i in ipv4)

print(is_valid_ipv4("192.168.1.1"))
print(is_valid_ipv4("255.01.50.111"))
print(is_valid_ipv4("255.00.50.111"))