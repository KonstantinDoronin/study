#проверка - есть ли значение из второго списка в первом списке и если есть - какой индекс


a = [int(i) for i in input().split()]#vvod posledovatelnostu chisev in list
b = int(input())#input int
c = []#empty list
d = 0#temporary variable
for i in range(0, len(a)): #ceycle to check int in list
    if b == a[i]:#uslovie
        c.append(i)#esly da - dobavlenie v cycle
        d += 1# scetchik
if d > 0:#cycle na proverke - est li hot odno sovpadenie
    for i in c:#output cycle like int continuously
        print(i, end=' ')
else:
    print('Отсутствует')

