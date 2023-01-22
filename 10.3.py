x_lim = 50
y_lim = 20
delta = 5
for row in range(y_lim):
    for col in range(x_lim):
        if row == 9:
            print('-', end='')
        elif col == 24:
            print('|', end='')
        elif col == x_lim//2-(row+delta):
            print('/', end='')
        elif col == x_lim//2 + (row + delta):
            print('\\', end='')
        else:
            print(' ', end='')
    print()        
            
