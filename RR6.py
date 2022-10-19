print("Вариант 1, задание 1")
n = int(input("Введите длину массива "))
a = []
for i in range(n):
	print("Введите", i, "элемент массива")
	a.append(int(input()))
print("Массив:", a)
Max = max(a)
Min = min(a)
a.reverse()
print("Массив в обратном порядке:", a)
print("Максимальное", Max)
print("Минимальное", Min)

print("Вариант 1, задание 2")

n = int(input("Введите длину массива "))
a = []
Sum = 0
for i in range(n):
	print("Введите", i, "элемент массива")
	a.append(float(input()))
	Sum = Sum + a[i]
print("Массив без замены первого элемента", a)
sr = Sum / n
a[0] = sr
print("Массив с заменой первого элемента", a)

print("Вариант 2, задание 1")

n = int(input("Введите длину массива "))
a = []
Min = 10 ** 20
i0 = 0
for i in range(n):
	print("Введите", i, "элемент массива")
	a.append(int(input()))
	if a[i] < Min:
		i0 = i
		Min = a[i]
print("Минимальное:", Min)
print("Индекс:", i0)

print("Вариант 2, задание 2")
n = int(input("Введите длину массива "))
a = []
a2 = []
a3 = []
for i in range(n):
	print("Введите", i, "элемент массива")
	a.append(int(input()))
for i in range(len(a)):
	if a[i] > 0:
		a2.append(a[i])
	else:
		a3.append(a[i])
print("1 массив:", a)
print("2 массив:", a2)
print("3 массив:", a3)

print("Вариант 3, задание 1")
n = int(input("Введите длину массива "))
a = []
Sum = 0
for i in range(n):
	print("Введите", i, "элемент массива")
	a.append(int(input()))
for i in range(len(a)):
	if i % 2 != 0:
		Sum = Sum + a[i]
print("Сумма элементов с нечетными индексами =", Sum)

print("Вариант 3, задание 2")
n = 8
a = []
k = 0
for i in range(n):
	print("Введите", i, "элемент массива")
	a.append(int(input()))
for i in range(len(a)):
	if a[i] < 15 :
		k = 2 * a[i]
		a[i] = k
print("Преобразованный массив: ", a)