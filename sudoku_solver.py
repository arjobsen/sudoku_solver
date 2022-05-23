# -*- coding: utf-8 -*-
"""

"""

sudoku = [
    [0,0,8,0,2,0,0,0,3],
    [0,0,0,0,7,8,0,0,9],
    [0,2,1,0,0,0,0,0,0],
    [0,0,0,9,0,0,0,0,0],
    [0,1,4,0,6,0,0,0,0],
    [2,0,6,0,0,0,0,0,0],
    [0,4,9,0,0,0,0,6,0],
    [7,0,2,0,0,0,4,0,8],
    [0,8,3,1,0,0,0,5,2]
]

# Vervang alle 0 met [1, 2, 3,... 9]
for row in range(9):
    for col in range(9):
        if sudoku[row][col] == 0:
            sudoku[row][col] = list(range(1,10))

# Print
progress = 0
for row in range(9):
    for col in range(9):
        if type(sudoku[row][col]) == int:
            # Correct getal
            progress += 1
            print(sudoku[row][col], end=' ')
        else:
            print('.', end=' ')
    print('')

print(f'\nCorrect: {progress}/81')



