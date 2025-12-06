"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2025-12-03                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def convert_list_item(markdown):
    markdown = markdown.strip()
    if not(markdown[0].isdigit()) or markdown[1] != ".":
        return "Invalid format"
    return "<li>"+markdown[2:].strip()+"</li>"
    


print(convert_list_item("1. My item"))
print(convert_list_item("A. last invalid"))