"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-01                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""


def sprawdz_sumy(grid,suma_do_uzyskania):
    if True in [sum(i) != suma_do_uzyskania for i in grid]:
        return False

    if True in [(grid[0][i] + grid[1][i] + grid[2][i]) != suma_do_uzyskania for i in range(len(grid[0]))]:
        return False

    if True in [grid[0][0] + grid[1][1] + grid[2][2],grid[0][2] + grid[1][1] + grid[2][0]] != suma_do_uzyskania:
        return False

def solve_magic_square(grid):
    brakujoca_liczba = 0
    suma_do_uzyskania = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                suma_do_uzyskania = max(sum(grid[0]),sum(grid[1]))
                grid[i][j] = suma_do_uzyskania - sum(grid[i])
                brakujoca_liczba = grid[i][j]
                break
                
    if(sprawdz_sumy(grid,suma_do_uzyskania) == False):
        return "impossible"

    return brakujoca_liczba

print(solve_magic_square([[2, 7, 6], [9, 0, 1], [4, 3, 8]]))