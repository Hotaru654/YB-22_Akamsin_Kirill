"""Вариант 1 Задание 1"""
def area(figure, data):
    if figure == 'круг':
        res = 3.14*(data[0]**2)
    if figure == 'прямоугольник':
        a,b = data
        res = a*b
    if figure == 'квадрат':
        res = data[0] * data[0]
    if figure == 'треугольник':
        a,b = data
        res = (a*b)/2
    return ' Площадь {} = {}'.format(figure, res)
    
figure = input('Фигура ')
data = [ float(i) for i in input('Введите данные через пробел ').rsplit()]
print(area(figure, data))

"""Вариант 1 Задание 2"""
def mass(Mass1, Mass2, Mass3):
    sr1 = 0
    sr2 = 0
    sr3 = 0
    Sum1 = 0
    Sum2 = 0
    Sum3 = 0
    for i  in range(len(Mass1)):
        Sum1 = Sum1 + Mass1[i]
    for j  in range(len(Mass2)):
        Sum2 = Sum2 + Mass2[j]
    for k  in range(len(Mass3)):
        Sum3 = Sum3 + Mass3[k]
    Sr1 = Sum1 / len(Mass1)
    Sr2 = Sum2 / len(Mass2)
    Sr3 = Sum3 / len(Mass3)
    return 'Среднее ариф. и сумма 1 массива:',Sr1, Sum1, 'Среднее ариф. и сумма 2 массива:', Sr2, Sum2, 'Среднее ариф. и сумма 3 массива:', Sr3, Sum3

Mass1 = [1,2,3,4,5,6,7,8,9]
Mass2 = [2,4,6,8,10]
Mass3 = [1,3,5,7,9]
print(mass(Mass1, Mass2, Mass3))

