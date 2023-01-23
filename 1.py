
n = int(input("Введите размер матрицы: "))

for a in range(n):
    for x in range(n):
        buf_x = (n - 1) - a  # вспомогательное число, которое будет уменьшаться от n-1 до 0
        if buf_x > x:
            print(0, end='')
        elif buf_x == x:
            print(1, end='')
        else:
            print(2, end='')
    print()

