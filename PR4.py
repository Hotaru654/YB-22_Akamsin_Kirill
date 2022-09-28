""" Задание # 1 """

a = int(input())
b = int(input())
for i in range(a, b + 1):
	print(i)

""" Задание # 2 """
a = int(input())
b = int(input())
if b < a:
	for i in range(a, b - 1, -1):
		print(i)	
elif a < b:
	for i in range(a, b + 1):
		print(i)

""" Задание # 3 """
a = int(input())
b = int(input())
for i in range(a, b + 1):
	if i % 2 != 0:
		print(i)

