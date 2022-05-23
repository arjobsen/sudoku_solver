# -*- coding: utf-8 -*-

from time import sleep

"""
SETUP
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

# Vervang alle 0 met {1, 2, 3,... 9}
for row in range(9):
    for col in range(9):
        if sudoku[row][col] == 0:
            sudoku[row][col] = set(range(1,10))

# Print
def print_sudoku():
    progress = 0
    for row in range(9):
        for col in range(9):
            if type(sudoku[row][col]) == int:
                # Correct
                progress += 1
                print(sudoku[row][col], end=' ')
            else:
                print('.', end=' ')
                # print(sudoku[row][col], end=' ')
        print('')
    
    print(f'\nIngevuld: {progress}/81')
    return progress


def invullen(sudoku):
    # Update sets met 1 enkele waarde naar ints
    for row in range(9):
        for col in range(9):
            if type(sudoku[row][col]) == set and len(sudoku[row][col]) == 1:
                sudoku[row][col] = list(sudoku[row][col])[0]
                
    return sudoku


"""
ITERATE
"""
i = 0
solved = False
while not solved:
    
    # print('Iteratie', i)
    progress = print_sudoku()
    if progress == 81:
        break
    i += 1
    
    # Algoritme 1
    # Uitsluiten van de al ingevulde getallen
    
    # Rijen
    for row in range(9):
        ingevulds = set(n for n in sudoku[row] if type(n) == int)
        # print(f'Ingevuld rij {row}:', ingevulds)
        
        # Weghalen ingevulde getallen
        for ingevuld in ingevulds:
            for col in range(9):
                if type(sudoku[row][col]) != int:
                    sudoku[row][col] = set(v for v in sudoku[row][col] if v != ingevuld)
    
    sudoku = invullen(sudoku)
    sleep(0.3)
    print_sudoku()    
    
    # Kolommen
    for col in range(9):
        ingevulds = set()
        for row in range(9):
            if type(sudoku[row][col]) == int:
                ingevulds = ingevulds | {sudoku[row][col]}
            
        # print(f'Ingevuld kolom {col}:', ingevulds)
        
        # Weghalen ingevulde getallen
        for ingevuld in ingevulds:
            for row in range(9):
                if type(sudoku[row][col]) != int:
                    sudoku[row][col] = set(v for v in sudoku[row][col] if v != ingevuld)
    
    sudoku = invullen(sudoku)
    sleep(0.3)
    print_sudoku()    
    
    # Vakken
    vak_ranges = [range(3), range(3,6), range(6,9)]
    for h_range in vak_ranges:
        for v_range in vak_ranges:
                    
            ingevulds = set()
            for row in h_range:
                for col in v_range:
                    if type(sudoku[row][col]) == int:
                        ingevulds = ingevulds | {sudoku[row][col]}
            
            # Weghalen ingevulde getallen
            for ingevuld in ingevulds:
                for row in h_range:
                    for col in v_range:
                        if type(sudoku[row][col]) != int:
                            sudoku[row][col] = set(v for v in sudoku[row][col] if v != ingevuld)
                    
            
    
    
    sudoku = invullen(sudoku)
    sleep(0.3)
    print_sudoku()
    
    # Dev break
    if i > 100:
        break