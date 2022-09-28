import math

""" Задание # 1 """
x = 14.26
y = -1.22
z = 3.5*10**-2
s = (2 * math.cos(x - 2/3)) / (1/2 + pow(math.sin(y), 2)) * (1 + (pow(z, 2) / 3 - pow(z, 2) // 5))
print("s = {0:.3f}".format(s))
