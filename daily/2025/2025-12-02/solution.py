"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2025-12-02                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

import re
def to_snake(camel):
    
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', camel).lower()

print(to_snake("helloWorld"))