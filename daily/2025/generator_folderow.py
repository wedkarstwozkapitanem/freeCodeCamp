import os
from datetime import date, timedelta

start = date(2025, 11, 24)
end = date(2025, 12, 12)

delta = timedelta(days=1)
current = start

while current <= end:
    folder_name = current.strftime("%Y-%m-%d")
    os.makedirs(folder_name, exist_ok=True)

    file_path = os.path.join(folder_name, "solution.py")

    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write('"""\n')
            f.write("  ==========================================\n")
            f.write("  || FreeCodeCamp – Daily Coding Challenge ||\n")
            f.write(f"  || Date: {current.strftime('%Y-%m-%d')}                      ||\n")
            f.write("  || Dominik Łempicki (kapitan)            ||\n")
            f.write("  ==========================================\n")
            f.write('"""\n\n')


    current += delta
