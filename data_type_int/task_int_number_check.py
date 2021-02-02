#ввод числа до тех пор, пока не будет введено овер 100
a = int(input())
while a <= 100:
    if 10 <= a <= 100:
        print(a)
    a = int(input())
    if a <= 10:
        continue
    if a > 100:
        break
