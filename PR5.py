""" Задание # 1 """
a = str(input())
k = 0
if a[0] == "Е" or a[0] == "е":
	k = k + 1
k = k + a.count(" Е")
k = k + a.count(" е")
print(k)
