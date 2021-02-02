#компрессия строки в зависимости от частоты элементов в ней
a = str(input())
cnt = 0
symb = a[0]
for i in a:#перевор всех значений строки
    s = i
    if symb == s:#счет значения
        cnt += 1
    else: #если в строке больше нет значения то выводим его на экран вместе с числом повторений
        print(str(symb) + str(cnt), end='')
        symb = i
        cnt = 1
    symb = s
print(str(symb) + str(cnt))
