"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-28                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def get_laptop_cost(laptops:list, budget:int) -> int:
    laptops = sorted(laptops,reverse=True)

    if laptops[1] <= budget:
        return laptops[1]
    
    return next((i for i in laptops if i <= budget),0)

print(get_laptop_cost([1500, 2000, 2000, 1800, 1400], 1900))
