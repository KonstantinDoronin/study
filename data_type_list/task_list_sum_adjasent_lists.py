#меняем исходных список на список состоящий из суммы соседних элементов значения списка
a = [int(i) for i in input().split()]
sum = 0
for i in range(0, len(a)):#перебор всех значений списка
    if len(a) == 1:#для единичного списка
        sum = a[0]
        print(sum, end='\t')
        continue
    if i + 1 < len(a):#для всех значений списка, кроме последнего
        sum = a[i - 1] + a[i + 1]
        print(sum, end='\t')
    if i + 1 == len(a):#для последнего значения списка
        sum = a[i - 1] + a[0]
        print(sum)
