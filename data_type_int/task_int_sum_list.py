#сумма элементов последовательности ввода
a = [int(i) for i in input().split()]
count = 0
for i in a:
    count += i
print(count)
