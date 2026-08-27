"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-27                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def evaluate(numbers:list, operators:list) -> int:
    nr_znak = int(0)
    wynik = int(numbers[0])

    for i,liczba in enumerate(numbers):
        if i == 0:
            continue
        znak = operators[nr_znak]
        if znak == '+':
            wynik += int(liczba)
        elif znak == '-':
            wynik -= int(liczba)
        elif znak == '*':
            wynik *= int(liczba)
        elif znak == '/':
            wynik /= int(liczba)
        elif znak == '%':
            wynik %= int(liczba)
        nr_znak += 1
        nr_znak %= len(operators)

    return wynik

print(evaluate([5, 6, 7, 8, 9], ['+', '-']))
print(evaluate([11, 4, 10, 17, 2], ['*', '*', '%']))