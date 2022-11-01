print('Вариант 1 Задание 1')
print("Введите кол-во строк и столбцов")
n = int(input())
a = []
k = 0
Sum = 0
h = 0
for i in range(n):
    b = []
    for j  in range(n):
        print('Введите [',i,',',j,'] элемент')
        b.append(int(input()))
    a.append(b)
for i in range(n):
    for j in range(h, n):
        if a[i][j] >  0:
            k  = k + 1
            Sum = Sum + a[i][j]
    h = h + 1
print("Сумма положительных эл.",Sum, "Кол-во положительных эл.", k)
for i in range(n):
    for j in range(n):
        print(a[i][j], end = '  ')
    print()

print('Вариант 1 Задание 2')
print("Введите кол-во строк ")
n = int(input())
print("Введите кол-во столбцов")
m = int(input())
a = []
Max = -10 ** 10
Min = 10 ** 10
for i in range(n):
    b = []
    for j  in range(m):
        print('Введите [',i,',',j,'] элемент')
        b.append(int(input()))
    a.append(b)
for i in range(n):
    for j in range(m):
        if a[i][j] >  Max:
            Max = a[i][j]
    for l in range(m):
        if a[i][l] <  Min:
            Min = a[i][l]
    a[i][-1] = Max
    a[i][0] = Min
    Min = 10 ** 10
    Max = -10 ** 10
for i in range(n):
    for j in range(n):
        print(a[i][j], end = '  ')
    print()

print('Вариант 2 Задание 1')
print("Введите кол-во строк и столбцов")
n = int(input())
a = []
k = 0
Sum0 = 0
Sum = 0
h = 0
o = 0
for i in range(n):
    b = []
    for j  in range(n):
        print('Введите [',i,',',j,'] элемент')
        b.append(int(input()))
    a.append(b)
for l in range(n):
    Sum0 = Sum0 + a[0][l]
for i in range(n):
    for j in range(n):
        Sum = Sum + a[i][j]
    if Sum != Sum0:
        h = h + 1
    Sum = 0
for j in range(n):
    for i in range(n):
        Sum = Sum + a[i][j]
    if Sum != Sum0:
        h = h + 1
    Sum = 0
for i in range(n):
    for j in range(n):
        print(a[i][j], end = '  ')
    print()
if h == 0:
    print('Матрица является магическим квадратом')
else:
    print('Матрица не является магическим квадратом')

print('Вариант 2 Задание 2')
print("Введите кол-во строк и столбцов")
n = int(input())
a = []
h1 = []
h2 = []
for i in range(n):
    b = []
    for j  in range(n):
        print('Введите [',i,',',j,'] элемент')
        b.append(int(input()))
    a.append(b)
for i in range(n):
    h1 = a[i][0]
    h2 = a[i][-1]
    a[i][0] = h2
    a[i][-1] = h1
for i in range(n):
    for j in range(n):
        print(a[i][j], end = '  ')
    print()