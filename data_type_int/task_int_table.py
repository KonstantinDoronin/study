#построение таблицы умножения вводимых значений по пределам (a-b - строки), (c-d) - столбцы
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for j in range(c, d+1): # построение верхней строки
    print('\t', j, end='')
for i in range(a, b + 1):#посторение строк
    print()#начальные значения строк
    print(i, end='\t')
    for j in range(c, d + 1): #сама центральная матрица умножения
        print(i * j, end='\t')
