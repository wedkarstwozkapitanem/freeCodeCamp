"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-31                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

import random

def generate_hex(color:str) -> str:
    wynik = "Invalid color"
    if color == "red":
        wynik = "FF"
        for _ in range(4):
            wynik += random.choice("0123456789ABCDEF")
    elif color == "green":
        wynik = ""
        for _ in range(2):
            wynik += random.choice("0123456789ABCDEF")
        wynik += ("FF")
        for _ in range(2):
            wynik += random.choice("0123456789ABCDEF")
    elif color == "blue":
        wynik = ""
        for _ in range(4):
            wynik += random.choice("0123456789ABCDEF")
        wynik += ("FF")

    return wynik

print(generate_hex("red"))