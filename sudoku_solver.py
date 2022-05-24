# -*- coding: utf-8 -*-

from time import sleep

"""
SETUP
"""

from sudoku_3_stars import sudoku_2 as sudoku

# Format sudoku string naar een nested list
sudoku = sudoku.split('\n')
sudoku = [s for s in sudoku if s]
sudoku = [[c for c in s] for s in sudoku]

# Vervang alle 0 met {1, 2, 3,... 9}
for row in range(9):
    for col in range(9):
        if sudoku[row][col] == '.':
            sudoku[row][col] = set(range(1,10))
        else:
            sudoku[row][col] = int(sudoku[row][col])

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
    
    print(f'\nIngevuld: {progress}/81\n\n\n')
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
    
    # Dev break
    if i > 10:
        print('BREAK')
        break
    
    # ALGORITME 1
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
    
    
    # ALGORITME 2
    # Als in 1 rij, kolom of vak maar 1 mogelijke plaats is voor een bepaald getal, vul die dan in
    
    # Rijen
    for row in range(9):
        opties = dict()
        ingevulds = set()
        for col in range(9):
            if type(sudoku[row][col]) != set:
                # Voeg bij ingevulds
                ingevulds.add(sudoku[row][col])
                continue
            
            # Leg de opties vast
            for v in sudoku[row][col]:
                if v not in opties.keys():
                    opties[v] = 1
                else:
                    opties[v] += 1
            
        # Nu loop nogmaals over de cellen en als het de enige optie is, vul die dan in
        for k, v in opties.items():
            if v == 1 and k not in ingevulds:
                for col in range(9):
                    if type(sudoku[row][col]) == set and k in sudoku[row][col]:
                        sudoku[row][col] = k
                        ingevulds.add(k)
                        break
                    
    sudoku = invullen(sudoku)
    sleep(0.3)
    print_sudoku()
    
    if sudoku[1][8] == 5:
        print("BREAK")
    
    
    # Kolommen
    for col in range(9):
        opties = dict()
        ingevulds = set()
        for row in range(9):
            if type(sudoku[row][col]) != set:
                # Voeg bij ingevulds
                ingevulds.add(sudoku[row][col])
                continue
            
            # Leg de opties vast
            for v in sudoku[row][col]:
                if v not in opties.keys():
                    opties[v] = 1
                else:
                    opties[v] += 1
            
        # Nu loop nogmaals over de cellen en als het de enige optie is, vul die dan in
        for k, v in opties.items():
            if v == 1 and k not in ingevulds:
                for row in range(9):
                    if type(sudoku[row][col]) == set and k in sudoku[row][col]:
                        sudoku[row][col] = k
                        ingevulds.add(k)
                        break            

    sudoku = invullen(sudoku)
    sleep(0.3)
    print_sudoku()
    
    if sudoku[1][8] == 5:
        print("BREAK")
    
    
    if i == 3:
        print("break")
    
    # Vakken
    vak_ranges = [range(3), range(3,6), range(6,9)]
    for h_range in vak_ranges:
        for v_range in vak_ranges:
                    
            ingevulds = set()
            opties = dict()
            for row in h_range:
                for col in v_range:
                    if type(sudoku[row][col]) == int:
                        ingevulds.add(sudoku[row][col])
                    
                    if type(sudoku[row][col]) == set:
                        # Leg de mogelijke opties van de cell vast
                        for v in sudoku[row][col]:
                            if v not in opties.keys():
                                opties[v] = 1
                            else:
                                opties[v] += 1
                        
            # Nu loop nogmaals over de cellen en als het de enige optie is, vul die dan in
            for k, v in opties.items():
                if v == 1 and k not in ingevulds:
                    for row in h_range:
                        for col in v_range:
                            if type(sudoku[row][col]) == set and k in sudoku[row][col]:
                                sudoku[row][col] = k
                                ingevulds.add(k)
                                
                                if sudoku[1][8] == 5:
                                    print("BREAK")
                                    
                                break  

    
    sudoku = invullen(sudoku)
    sleep(0.3)
    print_sudoku()
    
    if sudoku[1][8] == 5:
        print("BREAK")
    

