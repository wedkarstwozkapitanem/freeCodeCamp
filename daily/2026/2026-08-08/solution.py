"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-08                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def dfs(x,y,grid,szukany,odwiedzone):
    kierunki = [[0,1],[-1,0],[0,-1],[1,0]]
    if(grid[x][y] != szukany):
        return

    odwiedzone[x][y] = True
    for dx,dy in kierunki:
        x_t = x + dx
        y_t = y + dy
        if 0 <= x_t < len(grid) and 0 <= y_t < len(grid[0]) and not odwiedzone[x_t][y_t]:
            dfs(x_t,y_t,grid,szukany,odwiedzone)

def bucket_fill(grid, target_color):
    odwiedzone = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    licznik = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == target_color:
                continue
            if not odwiedzone[i][j]:
                dfs(i,j,grid,grid[i][j],odwiedzone)
                licznik += 1
    return licznik

print(bucket_fill([["R", "R"], ["R", "R"]], "G"))
print(bucket_fill([["B", "B", "B"], ["B", "B", "B"], ["B", "B", "B"]], "B"))
print(bucket_fill([["G", "Y", "Y"], ["G", "Y", "G"], ["Y", "Y", "G"]], "R"))
print(bucket_fill([["G", "G", "P", "Y"], ["O", "P", "P", "P"], ["O", "O", "P", "G"], ["G", "O", "O", "G"]], "P"))
print(bucket_fill([["G", "G", "C", "C", "O"], ["B", "Y", "B", "Y", "O"], ["B", "J", "O", "J", "B"], ["G", "Y", "Y", "Y", "B"], ["G", "P", "P", "G", "G"]], "Y"))