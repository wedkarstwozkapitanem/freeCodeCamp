"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2025-11-29                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def get_next_location(matrix):
    x1 = x2 = y1 = y2 = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                x1 = i
                y1 = j
            elif matrix[i][j] == 2:
                x2 = i
                y2 = j
    
    zx = x2 - x1
    zy = y2 - y1
    
    nx = x2 + zx
    ny = y2 + zy

    wynik = [x2+zx,y2+zy]
    if not(0 <= nx < len(matrix)):
        zx = -zx
        wynik[0] = zx + x2     
    
    if not(0 <= ny < len(matrix[0])):
        zy = -zy
        wynik[1] = zy + y2
        
   
    return wynik

print(get_next_location([[0,0,0,0], [0,0,0,0], [0,1,2,0], [0,0,0,0]]))