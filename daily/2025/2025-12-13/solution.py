"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2025-12-13                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def game_of_life(grid):

    kierunki = [
        [-1,-1],[-1,0],[-1,1],
        [0,-1],         [0,1],
        [1,-1],[1,0],[1,1],
    ];
    
    nowy = [[0] * len(grid[0]) for _ in range(len(grid))]
    for i in range(0,len(grid)):
        for j in range(0,len(grid[0])):
            liczbazywych = int(0)

            for p in kierunki:
                x = j + p[0]
                y = i + p[1]
                if(x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid)):
                    continue
                if(grid[y][x] == 1):
                    liczbazywych += 1

            if grid[i][j] == 1:
                if liczbazywych in (2,3):
                    nowy[i][j] = 1
            elif liczbazywych == 3:
                    nowy[i][j] = 1


    
    return nowy

print(game_of_life([[0, 1, 0], [0, 1, 1], [1, 1, 0]]))
