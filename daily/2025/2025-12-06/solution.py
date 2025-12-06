"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2025-12-06                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""


def format_date(date_string):
    miesioce = {
        "January":"01",
        "February":"02",
        "March":"03",
        "April":"04",
        "May":"05",
        "June":"06",
        "July":"07",
        "August":"08",
        "September":"09",
        "October":"10",
        "November":"11",
        "December":"12",
    }

    dane_daty = date_string.split(" ")
    
    data = str(dane_daty[2]) + '-' + str(miesioce[dane_daty[0]]) + '-'
    
    if len(dane_daty[1][:-1]) > 1:
        data += str(dane_daty[1][:-1])
    else:
        data += "0" + str(dane_daty[1][:-1])

    return data

print(format_date("December 6, 2025"))
print(format_date("September 7, 512"))