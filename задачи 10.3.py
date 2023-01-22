x_limit = 50
y_limit = 20
delta = 5
for row in range(y_limit):
    for col in range(x_limit):
        if row == 9:
            print('-', end = '')
        elif col == 24:
            print('|', end = '')
        elif col == x_limit//2 -(row + delta):
            print('/', end = '')
        elif col == x_limit//2 + (row + delta):
            print('\\', end = '')
        else:
            print(' ', end = '')
    print()        
            
