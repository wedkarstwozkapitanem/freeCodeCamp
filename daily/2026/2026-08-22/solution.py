"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-22                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def decode(message, shift):
    shift %= 26
    return "".join(
        chr((ord(i) - shift - 65) % 26 + 65) if i.isupper() 
        else chr((ord(i) - shift - 97) % 26 + 97) if i.islower() 
        else i
        for i in message
        )

print(decode("Xlmw mw e wigvix qiwweki.", 4))
print( decode("Byffi Qilfx!", 20))