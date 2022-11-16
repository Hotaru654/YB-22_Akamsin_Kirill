with open('Matrix.txt', 'r', encoding='utf-8-sig') as f:
	line = f.readlines()
	matrix = [element.replace("\n", "").split() for element in line]
n = len(matrix)
m = len(matrix[0])
a = matrix
f.close()
for p in range(n):
	for u in range(m):
		a[p][u] = int(a[p][u])
print(a)

#Вариант 1 Задание 1
k = 0
Sum = 0
h = 0
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
p = open('Result.txt', 'w')
for z in range(n):
	for v in range(n):
		l = str(a[z][v])
		p.write(l + '  ')
	p.write('\n')
p.write("Summa: " + str(Sum) + " Kol-vo polozhitelnih: " + str(k))
p.close()


#Вариант 1 Задание 2
Max = -10 ** 10
Min = 10 ** 10
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
p = open('Result.txt', 'w')
for z in range(n):
	for v in range(n):
		l = str(a[z][v])
		p.write(l + '  ')
	p.write('\n')
p.write('\n')
p.write("-------------")
p.close()

#Вариант 2 Задание 1
k = 0
Sum0 = 0
Sum = 0
h = 0
o = 0
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
p = open('Result.txt', 'w')
if h == 0:
    p.write('Матрица является магическим квадратом')
else:
    p.write('Матрица не является магическим квадратом')
p.close()

#Вариант 2 Задание 2
a = []
h1 = []
h2 = []
for i in range(n):
    h1 = a[i][0]
    h2 = a[i][-1]
    a[i][0] = h2
    a[i][-1] = h1
p = open('Result.txt', 'w')
for z in range(n):
	for v in range(n):
		l = str(a[z][v])
		p.write(l + '  ')
	p.write('\n')
p.write("Summa: " + str(Sum) + " Kol-vo polozhitelnih: " + str(k))
p.close()